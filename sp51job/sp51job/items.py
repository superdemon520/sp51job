# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Sp51JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name = scrapy.Field()
    job_company_name = scrapy.Field()
    job_place = scrapy.Field()
    job_salary = scrapy.Field()
    job_time = scrapy.Field()
    pass
