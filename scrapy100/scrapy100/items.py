from scrapy.item import Item, Field


class TitleItem(Item):
    title = Field()
    link = Field()
