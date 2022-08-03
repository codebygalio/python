# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import faker
import requests
from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

"""
    两个中间中间件都能够处理请求和响应, 但是使用场景不同
        DownloaderMiddleware: 下载中间件
            主要作用: 处理请求的cookies.headers请求头.设置请求代理
            
        SpiderMiddleware: 爬虫中间件
            主要作用: 过滤错误请求
        
"""
def get_proxy():
    """获取代理"""
    json_data = requests.get(url='http://127.0.0.1:5000/get/').json()
    proxy = json_data['proxy']
    return proxy


class Qd06DoubanSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class Qd06DoubanDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class HeadersDownloaderMiddleware:
    """headers中间件"""
    def process_request(self, request, spider):
        fake = faker.Faker()
        # request.headers拿到的是请求体的请求头, 是一个字典对象
        request.headers.update(
            {
                'Host': 'movie.douban.com',
                'User-Agent': fake.user_agent()
            }
        )
        return None


class CookiesDownloaderMiddleware:
    """cookies中间件"""
    def process_request(self, request, spider):
        cookies = {'Cookie': 'bid="xYzW76eUFk8"; __yadk_uid=XU38FA8bxpKrGZUK1KNEfbTp2VcwSYr4; __gads=ID=6db86c8088752a10-225dc67a68c40078:T=1603710897:RT=1603710897:S=ALNI_MaKwh8GKcMOamfPzR24mBE6kuNMoA; ll="118267"; gr_user_id=4fcfde02-4d08-47f3-a462-d0a6a8940853; _vwo_uuid_v2=DE17489458626A78A4431DB346C107A22|9aaf85c2d6c7f60e26ee63e6895d0949; douban-fav-remind=1; viewed="35236003"; __utmc=30149280; __utmz=30149280.1611126000.30.19.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=223695111; __utmz=223695111.1611126000.18.11.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1611142463%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D3ryrRbyBS5wKlUsfgsV-BWIl1dvDfobdEzpXVOu8haf14N95aMsJoBpfcQfmXDgc%26wd%3D%26eqid%3D91d486a50005661e000000066007d4f0%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.1097713080.1601989162.1611126000.1611142464.31; __utmb=30149280.0.10.1611142464; __utma=223695111.1702441161.1603710897.1611126000.1611142464.19; __utmb=223695111.0.10.1611142464; _pk_id.100001.4cf6=ce6b3b49020921cb.1603710897.19.1611144500.1611126699.'}
        # request.cookies拿到的是请求体的cookies, 是一个字典对象
        request.cookies.update(cookies)
        return None


class ProxyDownloaderMiddleware:
    """代理中间件"""
    def process_request(self, request, spider):
        # request.meta['proxy']  设置代理
        request.meta['proxy'] = get_proxy()
        return None

    """
    有事后代理质量不高, 代理请不到数据
    """