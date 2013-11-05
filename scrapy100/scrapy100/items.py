from scrapy.item import Item, Field


class WebSite(Item):
    given_url = Field()
    req_url = Field()
    resp_code = Field()
    desc = Field()
    keywords = Field()


class BankUrl(Item):
    domain = Field()
    given_url = Field()
    title = Field()
