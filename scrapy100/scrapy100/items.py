from scrapy.item import Item, Field


class WebSite(Item):
    url = Field()
    title = Field()
    desc = Field()
    keywords = Field()
