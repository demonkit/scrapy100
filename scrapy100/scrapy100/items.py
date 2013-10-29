from scrapy.item import Item, Field


class WebSite(Item):
    url = Field()
    title = Field()
    desc = Field()


class Keyword(Item):
    keyword = Field()
