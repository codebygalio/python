# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import requests
from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

"""
两个中间件都能处理请求和相应, 但是使用场景不同
    SpiderMiddleware: 爬虫中间件
        主要作用: 过滤一些错误请求, 框架会对异常的状态码自动过滤
        
    DownloaderMiddleware: 下载中间件
        主要作用: 处理请求的伪装: headers  cookies  proxies
"""


class Qd05DoubanSpiderMiddleware:
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


class Qd05DoubanDownloaderMiddleware:
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
    """请求头中间件"""
    def process_request(self, request, spider):
        # request 可以拿到请求体对象
        # request.headers 可以拿到请求体中的请求头, 是一个字典对象
        request.headers.update(
            {
                # cookies 在scrapy框架中会有专门的中间件
                # 'Cookie': 'bid=JOjnHzNKNdU; __gads=ID=390a3a70609550e8-22df6781f5d10053:T=1649854444:RT=1649854444:S=ALNI_MZfvUIHFs1pOYgYSuPbsvh7fVT9Yw; ll="118267"; _vwo_uuid_v2=D9BE563CAF8DB68077925251DB19E9857|7ec7c5b6350ccfad2f138472e47a6641; ct=y; _ga=GA1.2.1895635950.1649854444; gr_user_id=9841cb26-ad30-4da9-9fad-006c711b218f; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1653051308%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DhY0DMfkbQo_o8cDhG9yaanj86TmaZYpu_ThzggB88jy9Z209IF8iQNLi8ZWUDi5C%26wd%3D%26eqid%3Dd67d19310007283e0000000662878faa%22%5D; _pk_id.100001.4cf6=5a00c88162b3f1ff.1649854444.8.1653051308.1650890129.; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.1895635950.1649854444.1653051308.1653051308.1; __utmb=30149280.0.10.1653051308; __utmc=30149280; __utmz=30149280.1653051308.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.913704788.1649854444.1650890129.1653051308.8; __utmb=223695111.0.10.1653051308; __utmc=223695111; __utmz=223695111.1653051308.8.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __gpi=UID=0000059a569b8b1b:T=1653051309:RT=1653051309:S=ALNI_MboLjGTnG9YzoGaau8maDJk8dhE7A',
                'Host': 'movie.douban.com',
                'Referer': 'https://www.baidu.com/link?url=hY0DMfkbQo_o8cDhG9yaanj86TmaZYpu_ThzggB88jy9Z209IF8iQNLi8ZWUDi5C&wd=&eqid=d67d19310007283e0000000662878faa',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
            }
        )
        return None

class CookiesDownloaderMiddleware:
    """cookies中间件"""
    def process_request(self, request, spider):
        # request.cookies 拿到请求头中cookies, 也是一个字典对象
        # 如果整体的cookies没有用, 那么就需要把每一个片段的 cookies 分别构建
        request.cookies.update({'Cookie': 'bid=JOjnHzNKNdU; __gads=ID=390a3a70609550e8-22df6781f5d10053:T=1649854444:RT=1649854444:S=ALNI_MZfvUIHFs1pOYgYSuPbsvh7fVT9Yw; ll="118267"; _vwo_uuid_v2=D9BE563CAF8DB68077925251DB19E9857|7ec7c5b6350ccfad2f138472e47a6641; ct=y; _ga=GA1.2.1895635950.1649854444; gr_user_id=9841cb26-ad30-4da9-9fad-006c711b218f; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1653051308%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DhY0DMfkbQo_o8cDhG9yaanj86TmaZYpu_ThzggB88jy9Z209IF8iQNLi8ZWUDi5C%26wd%3D%26eqid%3Dd67d19310007283e0000000662878faa%22%5D; _pk_id.100001.4cf6=5a00c88162b3f1ff.1649854444.8.1653051308.1650890129.; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.1895635950.1649854444.1653051308.1653051308.1; __utmb=30149280.0.10.1653051308; __utmc=30149280; __utmz=30149280.1653051308.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.913704788.1649854444.1650890129.1653051308.8; __utmb=223695111.0.10.1653051308; __utmc=223695111; __utmz=223695111.1653051308.8.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __gpi=UID=0000059a569b8b1b:T=1653051309:RT=1653051309:S=ALNI_MboLjGTnG9YzoGaau8maDJk8dhE7A',})
        return None


def get_proxy():
    """获取代理的函数"""
    url = 'http://tiqu.pyhttp.taolop.com/getip?count=1&neek=13873&type=2&yys=0&port=1&sb=&mr=2&sep=0&ts=1'
    json_data = requests.get(url=url).json()

    # 在scrapy框架中, 代理只需要构建成  ip:端口  这样的形式
    proxies = "http://" + json_data['data'][0]['ip'] + ':' + str(json_data['data'][0]['port'])
    print('获取到的代理: ', proxies)
    return proxies

class ProxyDownloaderMiddleware:
    """proxies中间件"""
    def process_request(self, request, spider):
        # request.meta['proxy'] 设置代理
        print('设置代理:::', request.meta)
        request.meta['proxy'] = get_proxy()
        """设置代理目前做了更新操作, """
        return None

    """代理可能会有质量不高的情况"""
