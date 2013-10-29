#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------------------------------------
#  FileName :    title_spider.py
#  Author :      yuyang4@
#  Project :     PA
#  Date :        2013-10-27 17:31
#  Description : 
# -----------------------------------------------------


from scrapy.spider import BaseSpider


class TitleSpider(BaseSpider):
    name = 'titles'
    allowed_domains = ['http://wzjc.bjpc.gov.cn/', 'http://xczx.tax861.gov.cn/']
    start_urls = allowed_domains

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)
