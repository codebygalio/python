# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

"""
类字典对象
"""
class Qd03EnglishItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    info = scrapy.Field()
    img_url = scrapy.Field()
