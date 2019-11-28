import requests

from tools.mysql_connect import MysqlConnect


class Proxy(object):
    def __init__(self):
        con = MysqlConnect()
        self.connect = con.get_connect()

    def get_proxy_item(self):
        sql = "SELECT proxy_type, ip, port FROM proxies ORDER BY RAND() LIMIT 1;"
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        item = dict(
            proxy_type=result[0][0],
            ip=result[0][1],
            port=result[0][2]
        )
        is_effective = self.judge_ip(item)
        if is_effective:
            return item
        else:
            return self.get_proxy_item()

    def judge_ip(self, ip_item):
        http_url = 'https://www.lagou.com/'
        proxy_url = "{0}://{1}:{2}".format(ip_item['proxy_type'], ip_item['ip'], ip_item['port'])
        proxy_dict = {"{0}".format(ip_item['proxy_type']): proxy_url}
        try:
            response = requests.get(http_url, proxies=proxy_dict)
            print(response.text)
            status = response.status_code
            if 200 < status > 300:
                raise Exception('status_code:' + status)
        except Exception as e:
            print('invalid proxy', e)
            self.delete_ip(ip_item.ip)
            return False
        else:
            return True

    def delete_ip(self, ip):
        sql = "DELETE FROM proxies WHERE ip = {0}".format(ip)
        cursor = self.connect.cursor()
        result = cursor.execute(sql)
        self.connect.commit()

    def get_random_ip(self):
        ip_item = self.get_proxy_item()
        proxy_ip = "{0}://{1}:{2}".format(ip_item['proxy_type'].lower(), ip_item['ip'], ip_item['port'])
        print('proxy:', proxy_ip)
        return proxy_ip
