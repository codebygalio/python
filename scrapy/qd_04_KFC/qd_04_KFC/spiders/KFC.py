import scrapy

from ..items import Qd04KfcItem


class KfcSpider(scrapy.Spider):
    name = 'KFC'
    allowed_domains = ['kfc.com.cn']
    # start_urls = ['http://kfc.com.cn/']

    # 重写 start_urls
    def start_requests(self):
        # FormRequest 可以帮助我们发送post请求
        yield scrapy.FormRequest(url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword',
                             # 向服务器提交表单数据
                             formdata= {
                                        'cname':'',
                                        'pid':'',
                                        'keyword': '北京',
                                        'pageIndex': '1',
                                        'pageSize': '10'
                                    },
                             # meta参数: 在框架中用于两个函数间的数据传递
                             meta={'page': 2},
                             callback=self.parse)

    def parse(self, response):
        # print(response.text)
        print('上一个函数传下来的meta:', response.meta.get('page'))

        json_data = response.json()

        # 数据解析
        data_list = json_data['Table1']
        for da in data_list:
            storeName = da['storeName']
            cityName = da['cityName']
            addressDetail = da['addressDetail']
            pro = da['pro']

            yield Qd04KfcItem(storeName=storeName, cityName=cityName, addressDetail=addressDetail, pro=pro)

        # 处理翻页逻辑
        page = response.meta.get('page')
        if page <= 10:
            yield scrapy.FormRequest(url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword',
                                     formdata={
                                            'cname':'',
                                            'pid':'',
                                            'keyword': '北京',
                                            'pageIndex': str(page),
                                            'pageSize': '10'
                                        },
                                     meta={'page': page + 1},
                                     callback=self.parse
                                     )
