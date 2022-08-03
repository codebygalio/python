import scrapy

from ..items import Qd07Win4000Item


class Win4000Spider(scrapy.Spider):
    name = 'win4000_extend'
    allowed_domains = ['win4000.com']
    start_urls = ['http://www.win4000.com/meinv224632.html']

    def parse(self, response):
        # print(response.text)

        title = response.css('h1::text').get()
        urls = response.css('.pic-large::attr(src)').getall()  # 取列表

        item = Qd07Win4000Item(title=title, urls=urls)
        # 解析到的item先不返回
        # yield item

        next_page = response.css('.pic-next-img a::attr(href)').get()
        if next_page:
            yield scrapy.Request(next_page, callback=self.parse1, meta={'item': item})

    # 自定义的解析方法, response参数一定不能少
    def parse1(self, response):
        item = response.meta.get('item')  # 获取上一个函数传下来的item
        title = response.css('h1::text').get()  # 解析下一页图片的标题

        if title != item['title']:
            # 当你提取到的这一页 title, 不等于上一页的title
            # 意味着title发生了改变, 一个新的系列的图片就产生了
            yield item

            title = title  # 下一个系列的标题
            urls = response.css('.pic-large::attr(src)').getall() # 下一个系列的图片地址
            item = Qd07Win4000Item(title=title, urls=urls)
            next_page = response.css('.pic-next-img a::attr(href)').get()
            if next_page:
                yield scrapy.Request(next_page, callback=self.parse1, meta={'item': item})

        else:
            # 不满足if条件, 意味着这个系列的图片还没有采集完
            urls = response.css('.pic-large::attr(src)').getall()  # 下一个系列的图片地址
            # extend 是列表的合并方法
            item['urls'].extend(urls)
            next_page = response.css('.pic-next-img a::attr(href)').get()
            if next_page:
                yield scrapy.Request(next_page, callback=self.parse1, meta={'item': item})
