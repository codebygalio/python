import scrapy


from ..items import Qd02QuotesItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes_02'

    allowed_domains = ['toscrape.com']

    # 起始网址, 收集需要采集的所有URL地址,
    # 列表推导式
    # start_urls = [f'http://quotes.toscrape.com/page/{page}/' for page in range(1, 11)]
    # start_urls = ['http://quotes.toscrape.com/']

    def start_requests(self):
        """用来重写 start_urls 规则"""
        yield scrapy.Request(url='http://quotes.toscrape.com/', callback=self.parse)

    def parse(self, response):

        dis = response.css('.quote')

        for div in dis:
            text = div.css('.text::text').get()
            author = div.css('.author::text').get()
            tags = div.css('.tags a::text').getall()

            item = Qd02QuotesItem(text=text, author=author, tags=tags)
            yield item

        next_page = response.css('.next a::attr(href)').get()  # 下一页部分的url地址
        if next_page:
            next_url = 'http://quotes.toscrape.com' + next_page  # 完整的url地址
            print(next_url)

            # scrapy.Request 是一个请求对象
            # 构建好的请求对象, 同样的会交给下载器在互联网中下载资源, 也会返回一个 response 的响应体
            # callback  需要传入一个回调函数, 指定那个函数进行数据解析
            yield scrapy.Request(next_url, callback=self.parse)

    # def parse_2(self, response):
    #     pass

"""
构建翻页:
    方式1. scrapy.Request
        在我们不知道有多少页的情况下

    方式2. 在 start_urls列表里收集所有需要采集的地址
        在知道有多少页数据的情况下, 有翻页规律
"""
