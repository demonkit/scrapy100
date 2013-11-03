# -*- coding: utf-8 -*-
import json


from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import DropItem

import items
import models


class Scrapy100Pipeline(object):
    def __init__(self):
        engine = models.db_connect()
        models.createTable(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        if isinstance(item, items.WebSite):
            self._processWebSite(item, spider)
        elif isinstance(item, items.BankUrl):
            self._processBankUrl(item, spider)
        else:
            raise DropItem("type error, drop url: %s" % item['url'])

    def _processWebSite(self, item, spider):
        session = self.Session()
        try:
            web_site = models.WebSite.get(session, url=item['url'])
            web_site.desc=json.dumps(item['desc'])
            web_site.scrap_done = 1
            for kw in item['keywords']:
                web_site.keywords.append(
                        models.Keyword.get(session, kw))
            session.add(web_site)
            session.commit()
        except Exception, e:
            session.rollback()
            raise DropItem("db error, drop url: %s, since: %s" % (item['url'], e))
        finally:
            session.close()
        return item

    def _processBankUrl(self, item, spider):
        session = self.Session()
        try:
            web_site = models.WebSite(domain=item['domain'])
            web_site.title=item['title']
            web_site.scrap_done = 0
            session.add(web_site)
            session.commit()
        except Exception, e:
            session.rollback()
            raise DropItem("db error, drop url: %s, since: %s" % (item['domain'], e))
        finally:
            session.close()
        return item
