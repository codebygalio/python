import scrapy

from ..items import Qd09HuyaItem


class HuyaSpider(scrapy.Spider):
    name = 'huya'
    allowed_domains = ['huya.com']

    # start_urls = ['http://huya.com/']
    def start_requests(self):
        # 在scrapy框架中, 会对重复请求的url地址进行过滤
        yield scrapy.Request('https://www.huya.com/g/wzry')
        yield scrapy.Request('https://www.huya.com/g/wzry')
        yield scrapy.Request('https://www.huya.com/g/wzry')
        yield scrapy.Request('https://www.huya.com/g/wzry')

    def parse(self, response):
        # print(response.text)
        lis = response.css('.live-list.clearfix li')
        for li in lis:
            name = li.css('.nick::text').get()
            title = li.css('.title::text').get()
            img_url = li.css('.video-info img::attr(data-original)').get()

            item = Qd09HuyaItem(name=name, title=title, img_url=img_url)
            yield item
            # yield item
