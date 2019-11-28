# -*- coding: utf-8 -*-
import datetime

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from spider.items import LagouJobItemLoader, LagouJobItem
from tools.common import get_md5
from selenium import webdriver
# from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals


class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com/']

    # selenium 启动
    def __init__(self):
        chrome_settings = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_settings.add_experimental_option("prefs", prefs)
        self.browser = webdriver.Chrome(chrome_options=chrome_settings)
        super(LagouSpider, self).__init__()
        # signal
        # dispatcher.connect(self.spider_closed(), signals.spider_closed)

    # spider 退出时关闭chrome
    def spider_closed(self, spider):
        print('spider closed')
        self.browser.quit()

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        # signal
        spider = super(LagouSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(cls.spider_closed, signals.spider_closed)
        return spider

    rules = (
        Rule(LinkExtractor(allow=r'jobs/\d+.html.*'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'zhaopin/.*'), callback='call_test', follow=True),
        Rule(LinkExtractor(allow=r'gongsi/.*'), callback='call_test', follow=True),
    )

    def call_test(self, response):
        print('get test response:', response.url)
        text = response

    def parse_item(self, response):
        # 解析拉钩职位
        item_loader = LagouJobItemLoader(item=LagouJobItem(), response=response)
        item_loader.add_css("title", ".job-name::attr(title)")
        item_loader.add_value("url", response.url)
        item_loader.add_value("url_object_id", get_md5(response.url))
        item_loader.add_css("salary", ".job_request .salary::text")
        item_loader.add_xpath("job_city", "//*[@class='job_request']/h3/span[2]/text()")
        item_loader.add_xpath("work_years", "//*[@class='job_request']/h3/span[3]/text()")
        item_loader.add_xpath("degree_need", "//*[@class='job_request']/h3/span[4]/text()")
        item_loader.add_xpath("job_type", "//*[@class='job_request']/h3/span[5]/text()")
        item_loader.add_css("tags", ".position-label li::text")
        item_loader.add_css("publish_date", ".publish_time::text")
        item_loader.add_css('job_advantage', ".job-advantage p::text")
        item_loader.add_css('job_desc', '.job_bt div')
        item_loader.add_css('job_addr', '.work_addr a::text')
        item_loader.add_css('company_name', '#job_company dt a img::attr(alt)')
        item_loader.add_css('company_url', '#job_company dt a img::attr(alt)')
        item_loader.add_value('create_time', datetime.date.today())
        item = item_loader.load_item()

        return item
