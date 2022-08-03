import scrapy

from ..items import Qd08FulibaItem


class FulibaSpider(scrapy.Spider):
    name = 'fuliba'
    allowed_domains = ['fuliba2021.net']
    start_urls = [f'https://fuliba2021.net/page/{page}' for page in range(1, 162)]

    def parse(self, response):
        # print(response.text)
        # pass

        articles = response.css('.content article')

        for art in articles:
            title = art.css('h2 a::text').get()
            put_time = art.css('time::text').get()
            comments = art.css('.pc::text').get()
            starts = art.css('.post-like span::text').get()
            info = art.css('.note::text').get()
            yield Qd08FulibaItem(title=title, put_time=put_time, comments=comments,
                           starts=starts, info=info)



