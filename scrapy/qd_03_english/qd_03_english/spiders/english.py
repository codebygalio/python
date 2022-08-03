import scrapy

from ..items import Qd03EnglishItem

"""
收集所有需要采集的url地址
对每个地址返回的数据进行提取操作
"""


class EnglishSpider(scrapy.Spider):
    name = 'english'
    allowed_domains = ['chinadaily.com.cn']
    # 对于有规律的地址可以直接用列表推导式写在start_urls里面
    start_urls = [f'http://language.chinadaily.com.cn/thelatest/page_{page}.html' for page in range(1, 11)]

    # def start_requests(self):
    #     pass

    def parse(self, response):
        # print(response.text)
        divs = response.css('.gy_box')

        for div in divs:
           title = div.css('.gy_box_txt2>a::text').get().strip()
           info = div.css('.gy_box_txt3>a::text').get().strip()
           img_url = div.css('.gy_box_img>img::attr(src)').get()

           yield Qd03EnglishItem(title=title, info=info, img_url=img_url)

        # 构建下一页地址规律
        # yield scrapy.Request()




