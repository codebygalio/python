# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Qd04KfcItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    storeName = scrapy.Field()
    cityName = scrapy.Field()
    addressDetail = scrapy.Field()
    pro = scrapy.Field()
