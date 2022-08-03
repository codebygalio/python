import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        print(response.text)
        print(response.request.headers)
        """猜测: 可能遭遇到了反爬, 网络环境"""
