# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import datetime
import re

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join


class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


def remove_splash(value):
    return value.replace("/", "")


def compute_date(value):
    reg1 = '.*?(\d+-\d+-\d+)'
    reg2 = '.*?(\d+)天前'
    reg3 = '.*?(\d+:\d+)'
    result = re.match(reg1, value)
    if result:
        print('match1:', result.group(1))
        return result.group(1)

    result = re.match(reg2, value)
    if result:
        before = result.group(1)
        print('match1:', before)
        today = datetime.date.today()
        offset = datetime.timedelta(days=-int(before))
        re_day = (today + offset).strftime('%Y-%m-%d')
        return re_day

    result = re.match(reg3, value)
    if result:
        days = result.group(1)
        print('match3:', days)
        re_day = datetime.date.today()
        return re_day

    return None

class LagouJobItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class LagouJobItem(scrapy.Item):
    # 拉钩网职位信息
    title = scrapy.Field()
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    salary = scrapy.Field()
    job_city = scrapy.Field(
        input_processor=MapCompose(remove_splash)
    )
    work_years = scrapy.Field()
    degree_need = scrapy.Field(
        input_processor=MapCompose(remove_splash)
    )
    job_type = scrapy.Field()
    job_advantage = scrapy.Field()
    job_desc = scrapy.Field(
        input_processor=MapCompose(remove_splash)
    )
    job_addr = scrapy.Field()
    company_name = scrapy.Field()
    company_url = scrapy.Field()
    tags = scrapy.Field(
        input_processor=Join(",")
    )
    publish_date = scrapy.Field(
        input_processor=MapCompose(compute_date)
    )
    create_time = scrapy.Field()
    update_time = scrapy.Field()
