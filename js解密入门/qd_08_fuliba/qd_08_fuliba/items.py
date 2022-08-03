# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Qd08FulibaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    put_time = scrapy.Field()
    comments = scrapy.Field()
    starts = scrapy.Field()
    info = scrapy.Field()
