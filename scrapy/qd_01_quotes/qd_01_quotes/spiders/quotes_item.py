import scrapy

from ..items import Qd01QuotesItem


class QuotesItemSpider(scrapy.Spider):
    name = 'quotes_item'
    allowed_domains = []
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        divs = response.css('.quote')  # 获取所有符合条件的div标签

        for div in divs:
            text = div.css('.text::text').get()
            author = div.css('.author::text').get()
            tags = div.css('.tags>a::text').getall()


            # 把数据一条一条返回给item
            # 会默认在终端中打印一条一条数据字典
            yield Qd01QuotesItem(text=text, author=author, tags=tags)

            # yield {
            #     'text': text,
            #     'author': author,
            #     'tags': tags
            # }


