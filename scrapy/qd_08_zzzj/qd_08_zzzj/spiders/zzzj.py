import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


# 此模板会默认的继承自 CrawlSpider
from ..items import Qd08ZzzjItem


class ZzzjSpider(CrawlSpider):
    name = 'zzzj'
    allowed_domains = ['chinaz.com']
    # 根据一个起始网址, 爬取站点内的所有数据
    start_urls = ['https://top.chinaz.com/hangyemap.html']

    """
        rules           所有规则
        Rule            提取规则, 可以写多个, or 
        LinkExtractor   详细的提取规则(正则表达式)
    """
    rules = (
        # allow正则表达式的提取规则
        Rule(LinkExtractor(allow=r'http://top.chinaz.com/hangye/index.*?html',
                           # 限制住只在符合条件的标签里面进行提取, 优先级比allow的优先级要高, 需要传一个元组
                           restrict_css=('.Taleft', '.Taright')),
             callback='parse_item',  # callback回调, 传递回调函数名字的字符串形式
             follow=True  # 指定该规则荣response提取的连接, 是否需要跟进, 默认是跟进的
        ),

        # 规则2
        # Rule(LinkExtractor(allow=r'http://top.chinaz.com/hangye/index.*?html',
        #                    # 限制住只在符合条件的标签里面进行提取, 优先级比allow的优先级要高, 需要传一个元组
        #                    restrict_css=('.Taleft', '.Taright')),
        #      callback='parse_item',  # callback回调, 传递回调函数名字的字符串形式
        #      follow=True  # 指定该规则荣response提取的连接, 是否需要跟进, 默认是跟进的
        #      ),




        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # print(response.text)
        lis = response.css('.listCentent li')

        for li in lis:
            title = li.css('.rightTxtHead a::text').get()  # 网站名
            url = li.css('.col-gray::text').get()  # 网站url
            info = li.css('.RtCInfo::text').get().strip()  # 网站简介
            img_url = li.css('.leftImg a img::attr(src)').get()  # 网站图片地址

            item = Qd08ZzzjItem(title=title, url=url, info=info, img_url=img_url)
            yield item

        # 提取下一页部分连接
        next_page = response.css('.ListPageWrap a::attr(href)').getall()[-1]
        print('next_page', next_page)

        if next_page:
            all_url = 'https://top.chinaz.com/hangye/' + next_page
            print('all_url: ', all_url)
            yield scrapy.Request(all_url, callback=self.parse_item)


