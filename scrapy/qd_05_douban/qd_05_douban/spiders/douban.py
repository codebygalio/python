import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = []  # 不限制域名
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        print(response.text)
        print(response.request.headers)
        """猜测是不是遭遇到了反扒"""
