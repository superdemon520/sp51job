# -*- coding: utf-8 -*-
import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['www.51job.com']
    start_urls = ['http://www.51job.com/']

    def parse(self, response):
        pass
