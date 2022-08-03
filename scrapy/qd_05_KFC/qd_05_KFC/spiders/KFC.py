import scrapy
from scrapy import FormRequest

from ..items import Qd05KfcItem


class KfcSpider(scrapy.Spider):
    name = 'KFC'
    allowed_domains = ['kfc.com.cn']
    # start_urls = ['http://kfc.com.cn/']

    def start_requests(self):
        yield scrapy.FormRequest('http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword',
                                 formdata={
                                    'cname': '',
                                    'pid': '',
                                    'keyword': '北京',
                                    'pageIndex': '1',
                                    'pageSize': '10',
                                 },
                                 callback=self.parse,
                                 # 用来翻页
                                 meta={'page': 2}

                                 )
        """
             meta 用于两个函数之间传递参数
             meta 一次性的, 每一次创建requests对象都会重新创建
             meta 是一个字典
         """

    def parse(self, response):
        json_data = response.json()

        data_list = json_data['Table1']

        for data in data_list:
            storeName = data['storeName']
            addressDetail = data['addressDetail']
            pro = data['pro']
            cityName = data['cityName']

            item = Qd05KfcItem(storeName=storeName, addressDetail=addressDetail, pro=pro, cityName=cityName)
            yield item

        print('传下来的meta: ',response.meta.get('page'))

        page = response.meta.get('page')
        if page <= 7:
            yield scrapy.FormRequest('http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword',
                                     formdata={
                                        'cname': '',
                                        'pid': '',
                                        'keyword': '北京',
                                        'pageIndex': str(page),
                                        'pageSize': '10',
                                     },
                                     callback=self.parse,
                                     # 用来翻页
                                     meta={'page': page + 1}
                                     )

    def parse2(self, response):
        pass

    def parse3(self, response):
        pass