# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import re

from tools.mysql_connect import MysqlConnect

mysql_connect = MysqlConnect()


class SpiderPipeline(object):
    def process_item(self, item, spider):
        return item


# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
class LagouMysqlPipeline(object):
    # 采用同步的机制写入mysql
    def __init__(self):
        self.con = mysql_connect.get_connect()
        self.cursor = self.con.cursor()

    def process_item(self, item, spider):
        reg = '.*?(\d+)k-(\d+)k'
        reg_match = re.match(reg, item['salary'])
        salary_min = 0
        salary_max = 0
        try:
            salary_max = int(reg_match.group(2) + '000')
        except Exception as e:
            print('salary pick error', e)
        try:
            salary_min = int(reg_match.group(1) + '000')
        except Exception as e:
            print('salary pick error', e)
        insert_sql = "INSERT INTO `lagou_jobs`(title, url, url_object_id, salary_min, salary_max, job_city, " \
                     "work_years, degree_need, job_type, tags, publish_date, job_advantage, job_desc, job_addr, " \
                     "company_name, company_url) " \
                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(insert_sql, (
            item["title"], item["url"], item['url_object_id'], salary_min, salary_max, item["job_city"],
            item["work_years"],
            item["degree_need"], item["job_type"], item["tags"], item["publish_date"],
            item["job_advantage"], item["job_desc"], item["job_addr"], item["company_name"], item["company_url"]))
        self.con.commit()
