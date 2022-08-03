import scrapy
from scrapy_redis.spiders import RedisSpider


# 继承自RedisSpider
from ..items import Qd10FxtItem


class FxtSpider(RedisSpider):
    name = 'fxt'
    allowed_domains = ['fang.com']
    # start_urls = ['http://fang.com/']

    # 通过redis数据库向爬虫框架分发任务
    redis_key = 'fang:url'


    def parse(self, response):
        trs = response.css('#c02 tr')  # 获取57个tr标签

        province = None
        for tr in trs:
            pro = tr.css('td[valign="top"] strong::text').get()

            if pro:
                # 判断有没有获取省份
                if pro.strip(): # 目的是防止获取到空省份
                    province = pro

            if province == '其他':
                continue

            # 获取城市信息
            city_a = tr.css('td a')
            for city in city_a:
                # 获取城市名字
                city_name = city.css('a::text').get()
                # 获取城市URL地址
                city_url = city.css('a::attr(href)').get()
                yield scrapy.Request(url=city_url,
                                     callback=self.parse_city,
                                     meta={
                                         'province': province,
                                         'city_name': city_name
                                     }
                                     )

    def parse_city(self, response):
        """过程   由城市页面  解析到新房的url地址"""
        new_house_url = response.css('#dsy_D01_02 div.s4Box a::attr(href)').get()
        if new_house_url:
            yield scrapy.Request(url=new_house_url,
                                 callback=self.parse_new_house,
                                 # 上一个函数没用到的meta, 继续传递到下一个函数
                                 meta=response.request.meta)


    def parse_new_house(self, response):
        province = response.request.meta.get('province')
        city_name = response.request.meta.get('city_name')

        # 数据解析
        lis = response.css('.nl_con>ul>li')
        for li in lis:
            name = li.css('.nlcd_name a::text').get()
            if name:
                name = name.strip()

            price = li.css('.nhouse_price span::text').get()
            room = li.css('.house_type a::text').getall()
            area = li.css('.house_type::text').re('[\d~平米]+')
            sale = li.css('.fangyuan span::text').get()
            origin_url = li.css('.nlcd_name a::attr(href)').get()

            item = Qd10FxtItem(province=province, city_name=city_name, name=name, price=price,
                        room=room, area=area, sale=sale, origin_url=origin_url)

            yield item

            # 构建翻页
