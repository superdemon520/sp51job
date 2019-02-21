# -*- coding: utf-8 -*-
import time
import scrapy
from ..items import *
from lxml import etree
from scrapy.http import Request
from scrapy.selector import Selector 
from scrapy.spiders import CrawlSpider


class JobspiderSpider(scrapy.Spider):
    name = 'jobspider'
    # allowed_domains = ['www.51job.com']
    start_urls = ['https://search.51job.com/list/010000,000000,0000,00,9,99,%25E7%2588%25AC%25E8%2599%25AB,2,1.html']

    def parse(self, response):
        titles = []
        companies = []
        regions = []
        salaries = []
        times = []

        item = Sp51JobItem()
        job_div_list = response.xpath("//div[@id='resultList']/div[@class='el']")
        for job_div in job_div_list:
            job_name = job_div.xpath("p/span/a/@title").extract_first('无工作名称').strip().replace(",", "/")
            job_company_name = job_div.xpath("span[@class='t2']/a/@title").extract_first('无公司名称').strip()
            job_place = job_div.xpath("span[@class='t3']/text()").extract_first('无地点名称').strip()
            job_salary = job_div.xpath("span[@class='t4']/text()").extract_first('面议').strip()
            job_time = job_div.xpath("span[@class='t5']/text()").extract_first('无时间信息').strip()
            item['job_name'] = job_name
            item['job_company_name'] = job_company_name
            item['job_place'] = job_place
            item['job_salary'] = job_salary
            item['job_time'] = job_time
            yield item
        if len(response.xpath("//div[55]/div/div/div/ul/li[8]/a/@href"))>0:
            nextpg = response.xpath("//div[55]/div/div/div/ul/li[8]/a/@href").extract()[0]
            yield Request(nextpg,callback=self.parse)
