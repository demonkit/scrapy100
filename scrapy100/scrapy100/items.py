from scrapy.item import Item, Field


class WebSite(Item):
    url = Field()
    desc = Field()
    keywords = Field()


class BankUrl(Item):
    domain = Field()
    title = Field()
