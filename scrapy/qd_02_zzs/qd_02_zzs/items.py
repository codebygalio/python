# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Qd02ZzsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 标题
    info = scrapy.Field()  # 简介
    reads = scrapy.Field()  # 阅读数
    commons = scrapy.Field()  # 评论数
