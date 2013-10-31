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
        if not isinstance(item, items.WebSite):
            raise DropItem("type error, drop url: %s" % item['url'])
        objs = []
        web_site = models.WebSite(
                url=item['url'], title=item['title'],
                desc=json.dumps(item['desc']))
        objs.append(web_site)
        for kw in item['keywords']:
            objs.append(models.Keyword(keyword=kw))
        try:
            session.add_all(objs)
            session.commit()
        except Exception, e:
            session.rollback()
            raise DropItem("db error, drop url: %s, since: %s" % (item['url'], e))
        finally:
            session.close()
        return item
