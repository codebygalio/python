import scrapy


# .. 表示取上一级目录
from ..items import Qd02QuotesItem

"""
1. 收集需要采集的url地址
2. 解析数据
"""


# scrapy.Spider 爬虫的基类
class QuotesSpider(scrapy.Spider):
    # 爬虫项目的名字
    name = 'quotes'

    # allowed_domains 对站点的域名进行限制
    allowed_domains = ['toscrape.com']

    # 采集网址的起始地址
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # response = 响应体(requests.response) + parsel.Selector
        # print(response.text)
        # pass

        dis = response.css('.quote')

        for div in dis:
            text = div.css('.text::text').get()
            author = div.css('.author::text').get()
            tags = div.css('.tags a::text').getall()
            # print(text, author, tags)

            # 数据解析返回的是一个字典对象, scrapy框架会自动的进行处理
            # 爬虫文件的数据返回全部是使用yield
            # yield {
            #     'text': text,
            #     'author': author,
            #     'tags': tags,
            # }

            item = Qd02QuotesItem(text=text, author=author, tags=tags)
            # 一条一条返回解析出来的数据
            yield item
