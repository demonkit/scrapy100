#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from scrapy100.items import WebSite


class KeywordSpider(BaseSpider):
    name = 'keyword'
    allowed_domains = ['http://www.cmbc.com.cn']
    start_urls = allowed_domains

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        # parse title
        web_item = WebSite()
        web_item['url'] = response.url
        web_item['title'] = hxs.select("/html/head/title/text()")[0].extract()
        web_item['desc'] = []
        web_item['keywords'] = []

        # parse descriptions
        desc_selectors = hxs.select("/html/head/meta[@name='description']")
        for desc in desc_selectors:
            web_item['desc'].append(desc.select("@content")[0].extract().encode("utf-8"))

        # parse keywords
        keywords = hxs.select("/html/head/meta[@name='keywords']")
        for k_word in keywords:
            words = ''
            words = k_word.select("@content")[0].extract()
            web_item['keywords'].extend(words.split(','))
        web_item['keywords'] = list(set(web_item['keywords']))

        return [web_item]
