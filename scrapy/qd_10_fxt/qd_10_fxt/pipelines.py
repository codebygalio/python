# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv

import pymongo
from itemadapter import ItemAdapter


class MongodbPipeline:
    def __init__(self):
        # 1. 指定连接数据库
        self.client = pymongo.MongoClient(host='106.52.167.142',
                                     port=27017)

        # 2. 指定用哪一个数据库
        self.collections = self.client.test

        # 3. 指定操作的文档
        self.data = self.collections.data

    def process_item(self, item, spider):
        self.data.insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()
