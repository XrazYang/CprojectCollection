# -*- coding: utf-8 -*-
import scrapy.cmdline
from CprojectCollection.items import CprojectcollectionItem
import os


# https://github.com/search?l=C&p=1&q=C&type=Repositories
class Ccollection(scrapy.Spider):
    name = "CprojectCollection"
    allowed_domains = ["github.com"]

    def __init__(self):
        self.start_urls = []
        for i in range(1, 101):
            # https://github.com/search?l=C&o=desc&p=2&q=C&s=stars&type=Repositories
            url = "https://github.com/search?l=C&o=desc&p=" + str(i) + "&q=C&s=stars&type=Repositories"
            self.start_urls.append(url)

    def parse(self, response):
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
        # time.sleep(5)


if __name__ == '__main__':
    if os.path.exists("project_list.csv"):
        os.remove('project_list.csv')
    scrapy.cmdline.execute(['scrapy', 'crawl', 'CprojectCollection', '-o', 'project_list.csv'])
