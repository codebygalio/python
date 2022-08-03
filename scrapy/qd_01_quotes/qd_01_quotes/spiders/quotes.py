import scrapy


class QuotesSpider(scrapy.Spider):
    # 爬虫文件的名字, 通过scrapy genspider时创建的, 后面可以改, 而且运行项目要根据名字运行
    name = 'quotes'

    # 运行项目时, 对采集网站的域名地址做一个限制, 只会采集该域名下的数据, 可以删除, 不限制
    # 允许的范围是一个列表, 可以写多个域名做限制
    allowed_domains = []

    # 起始网址, 从这个网址进行采集, 是自动生成的, 一般是错误的
    # 介入数据采集的网址是有规律的, 可以用列表推导式构建所有需要采集的地址
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # response = 具备所有响应体数据 + 所有数据解析的方法
        # print(response.text)

        divs = response.css('.quote')  # 获取所有符合条件的div标签

        for div in divs:
            text = div.css('.text::text').get()
            author = div.css('.author::text').get()
            tags = div.css('.tags>a::text').getall()

            # 在爬虫文件里面, 所有数据, 全部用yield返回
            # 针对字典数据返回, scrapy 框架会自动处理
            # 一条一条返回数据
            yield {
                'text': text,
                'author': author,
                'tags': tags
            }

"""
假如有反扒, 怎么解决?
如何保存数据?
框架内部调用的顺序是什么样子?
"""