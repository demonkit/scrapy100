# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


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
            obj = models.WebSite(**item)
        elif isinstance(item, items.Keyword):
            obj = models.Keyword(**item)
        else:
            raise DropItem("type error, drop url: %s" % item['url'])
        try:
            session.add(obj)
            session.commit()
        except Exception, e:
            session.rollback()
            raise DropItem("db error, drop url: %s" % item['url'])
        finally:
            session.close()
        return item
