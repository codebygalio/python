# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# 定义数据结构的
# 继承自scrapy.Item
# 类字典对象, 提供了额外的保护机制
class Qd02QuotesItem(scrapy.Item):
    # define the fields for your item here like:
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()


"""
定义多个数据结构
"""
