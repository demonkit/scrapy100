#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from scrapy100.items import WebSite, Keyword


class KeywordSpider(BaseSpider):
    name = 'keyword'
    allowed_domains = ['http://www.cmbc.com.cn', 'http://www.cmbchina.com']
    start_urls = allowed_domains

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        items = []

        # parse title
        web_item = WebSite()
        web_item['url'] = response.url
        web_item['title'] = hxs.select("/html/head/title/text()")[0].extract()
        # parse descriptions
        desc_selectors = hxs.select("/html/head/meta[@name='description']")
        web_item['desc'] = []
        for desc in desc_selectors:
            web_item['desc'].append(desc.select("@content")[0].extract())
        items.append(web_item)

        # parse keywords
        keywords = hxs.select("/html/head/meta[@name='keywords']")
        for k_word in keywords:
            words = k_word.select("@content")[0].extract()
            for kw in words.split(','):
                kw_item = Keyword()
                kw_item['keyword'] = kw
                items.append(kw_item)

        return items
