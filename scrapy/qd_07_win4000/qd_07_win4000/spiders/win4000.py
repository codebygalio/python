import scrapy

from ..items import Qd07Win4000Item


class Win4000Spider(scrapy.Spider):
    name = 'win4000'
    allowed_domains = ['win4000.com']
    start_urls = ['http://www.win4000.com/meinv224632.html']

    def parse(self, response):
        # print(response.text)

        title = response.css('h1::text').get()
        urls = response.css('.pic-large::attr(src)').get()

        item = Qd07Win4000Item(title=title, urls=urls)
        yield item

        next_page = response.css('.pic-next-img a::attr(href)').get()
        if next_page:
            yield scrapy.Request(next_page, callback=self.parse)