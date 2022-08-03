import scrapy

from ..items import Qd01QuotesItem


class QuotesNextSpider(scrapy.Spider):
    name = 'quotes_next'
    allowed_domains = []

    # 把有规律的地址可以放入start_urls里面
    # start_urls = [f'https://quotes.toscrape.com/page/{i}/'for i in range(1, 11)]

    # 相当于start_urls
    def start_requests(self):
        yield scrapy.Request(url='https://quotes.toscrape.com/', callback=self.parse)


    def parse(self, response):
        divs = response.css('.quote')  # 获取所有符合条件的div标签

        for div in divs:
            text = div.css('.text::text').get()
            author = div.css('.author::text').get()
            tags = div.css('.tags>a::text').getall()

            yield Qd01QuotesItem(text=text, author=author, tags=tags)

        """处理翻页"""
        next_page = response.css('.next>a::attr(href)').get()  # 部分地址

        if next_page:
            # 完整地址
            all_url = 'https://quotes.toscrape.com' + next_page

            print('构建的地址:', all_url)
            # scrapy.Request  构建请求体对象
            # callback 构建的请求体, 返回的数据, 交给那个函数做处理
            yield scrapy.Request(url=all_url, callback=self.parse)
