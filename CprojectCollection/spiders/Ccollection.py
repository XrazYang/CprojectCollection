# -*- coding: utf-8 -*-
import scrapy.cmdline
from CprojectCollection.items import CprojectcollectionItem
from scrapy.http import Request
import time
import os


# https://github.com/search?l=C&p=1&q=C&type=Repositories
class Ccollection(scrapy.Spider):
    name = "CprojectCollection"
    allowed_domains = ["github.com"]
    start_urls = ["https://github.com/search?l=C&o=desc&p=1&q=C&s=stars&type=Repositories"]

    def parse(self,response):
        item = CprojectcollectionItem()

        project_list = response.xpath('//a[@class="v-align-middle"]/@href')
        for project_name in project_list:
            project = str(project_name.extract())
            i = project.rfind("/")
            user_name = project[1:i]
            project_name = project[i + 1:]
            item["user_name"] = user_name
            item["project_name"] = project_name
            item["project_url"] = "git@github.com:" + project[1:] + ".git"
            yield item

            #'//a[@class="next_page"]/@href'
        next_page_args = response.xpath('//a[@class="next_page"]/@href').extract()
        if next_page_args:
            next_page = "https://github.com"+next_page_args[0]
            print(next_page)
            time.sleep(10)
            yield Request(next_page, callback=self.parse)


if __name__ == '__main__':
    if os.path.exists("project_list_C.csv"):
        os.remove('project_list_C.csv')
    scrapy.cmdline.execute(['scrapy', 'crawl', 'CprojectCollection', '-o', 'project_list_C.csv'])
