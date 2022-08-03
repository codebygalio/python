# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'


# 去重组件   scrapy_redis实现的去重的方案
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# SCHEDULER 修改的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 开启数据持久化(把爬取过的数据保存下来)
SCHEDULER_PERSIST = True
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,

    # 把数据保存到redis数据库(请求体, item数据结构, 生成请求体的指纹)
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 1


# 如果没有设置redis数据库, 默认使用的本地的
# redis数据库的配置
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
