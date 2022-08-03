import scrapy

from ..items import Qd04GuokeItem


class GuokeSpider(scrapy.Spider):
    name = 'guoke'
    allowed_domains = ['guokr.com']
    start_urls = [f'https://www.guokr.com/i/1948640618/answers/?page={page}' for page in range(1, 17)]

    def parse(self, response):
        lis = response.css('.answer_list li')

        for li in lis:
            title = li.css('h4 a::text').get()
            href = li.css('h4 a::attr(href)').get()
            info = li.css('p::text').get()
            support = li.css('span::text').get()

            item = Qd04GuokeItem(title=title, href=href, info=info, support=support)
            yield item

