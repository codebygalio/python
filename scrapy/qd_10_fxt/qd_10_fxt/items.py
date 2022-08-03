# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Qd10FxtItem(scrapy.Item):
    # define the fields for your item here like:
    province = scrapy.Field()  # 省份
    city_name = scrapy.Field()  # 城市名
    name = scrapy.Field()  # 楼盘名
    price = scrapy.Field()  # 价格
    room = scrapy.Field()  # 几居室
    area = scrapy.Field()  # 面积
    sale = scrapy.Field()  # 是否在售
    origin_url = scrapy.Field()  # 详情页URL地址
