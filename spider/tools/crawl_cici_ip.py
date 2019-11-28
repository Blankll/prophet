import random
import time

import requests
from fake_useragent import UserAgent
from scrapy import Selector

from tools.mysql_connect import MysqlConnect
from tools.proxy import Proxy

mysql_connect = MysqlConnect()
con = mysql_connect.get_connect()
dbcursor = con.cursor()

proxy = Proxy()


def crawl_ips():
    # 爬取西刺的免费ip
    ua = UserAgent()
    headers = {
        "User-Agent": ua.random
    }

    def get_pages():
        # meta = proxy.get_random_ip()
        resp = requests.get("https://www.xicidaili.com/nn/1", headers=headers)
        selector = Selector(text=resp.text)
        pages = selector.css('.pagination a::text').extract()
        return int(pages[len(pages) - 2])

    page_num = get_pages()
    for i in range(200, page_num):
        time.sleep(random.randint(20, 60))
        resp = requests.get("https://www.xicidaili.com/nn/{0}".format(i), headers=headers)
        # print(resp.text)
        selector = Selector(text=resp.text)
        all_trs = selector.css('#ip_list tr')
        for tr in all_trs[1:]:
            all_txt = tr.css("td")
            ip = all_txt[1].css('*::text').get()
            port = all_txt[2].css('*::text').get()
            serve_addr = all_txt[3].css('a::text').get()
            desc = all_txt[4].css('*::text').get()
            proxy_type = all_txt[5].css('*::text').get()
            speeds = tr.css('.bar::attr(title)').extract()
            speed = 0
            if speeds[0]:
                speed = float(speeds[0].split('秒')[0])
            connect_time = 0
            if speeds[1]:
                connect_time = float(speeds[1].split('秒')[0])
            # live_time = all_txt[8].css('*::text').get()
            # live_time = re.match('(^[\d\.]+)\w*', live_time).group(1)
            validate_time = '20' + all_txt[9].css('*::text').get()
            try:
                sql = "INSERT INTO proxies(`ip`, `port`, `serve_addr`, `desc`, `proxy_type`, `speed`, `connect_time`, " \
                      "`validate_time`) " \
                      "VALUES ('{0}', {1}, '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')" \
                    .format(ip, port, serve_addr, desc, proxy_type, speed, connect_time, validate_time)
                dbcursor.execute(sql)
                print('insert success')
            except Exception as e:
                print('insert proxy failure')
        try:
            con.commit()
        except Exception as e:
            print('commit data failure')
        pass
        print('insert after')
    pass


crawl_ips()
