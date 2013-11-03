#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

import gurl
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from sqlalchemy.orm import sessionmaker

from scrapy100 import items
from scrapy100 import models

def getWebSites():
    engine = models.db_connect()
    session = sessionmaker(bind=engine)()
    return session.query(models.WebSite).filter(models.WebSite.scrap_done==0)


def cookUrls(websites):
    start_urls = []
    for site in websites:
        url = site.url
        if not url:
            continue
        start_urls.append(url)
    return start_urls


def cookDomains(urls):
    domains = []
    for u in urls:
        domains.append(gurl.Url(u).host.domain)
    return domains


class KeywordSpider(BaseSpider):
    name = 'keyword'
    try:
        start_urls = cookUrls(getWebSites())
        allowed_domains = cookDomains(start_urls)
    except:
        start_urls = []
        allowed_domains = []

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        web_item = items.WebSite()
        web_item['req_url'] = response.url
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
