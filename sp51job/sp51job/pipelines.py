# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Sp51JobPipeline(object):
    def process_item(self, item, spider):
    	with open("jobspider.txt",'a') as fp:
            fp.write(
            	item['job_name'] + ',' +
                item['job_company_name'] + ',' +
                item['job_place'] + ',' +
                item['job_salary'] + ',' +
                item['job_time'] + '\n')
