#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from scrapy100.items import BankUrl


class BankSpider(BaseSpider):
    name = 'bank'
    allowed_domains = ['www.china-cba.net']
    start_urls = ['http://www.china-cba.net/']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        # parse bank domain
        # select is the outer wrapper of all options
        select = hxs.select("/html/body/div[6]/div[2]//select")[0]
        options = select.select("option")
        items = []
        for opt in options[1:]:
            url_attr = opt.select("@value")
            if not url_attr:
                bank = BankUrl()
            else:
                bank = BankUrl(url=url_attr[0].extract())
            bank['title'] = opt.select("text()")[0].extract()
            items.append(bank)

        return items
