import scrapy

from ..items import Qd07MaoyanItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://m.maoyan.com/board/4']

    def parse(self, response):
        # print(response.text)

        divs = response.css('.board-card')  # 所有的div标签
        # print(divs)
        for div in divs:
            name = div.css('.title::text').get()
            star = div.css('.info>div.actors::text').get()
            releasetime = div.css('.date::text').get()
            score = div.css('.number::text').get()
            yield Qd07MaoyanItem(name=name, star=star, releasetime=releasetime, score=score)


