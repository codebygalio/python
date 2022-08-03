# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
import hashlib
import json

from itemadapter import ItemAdapter


filter_list = []

class Qd09HuyaPipeline:
    def __init__(self):
        self.f = open('data.csv', mode='a', encoding='utf-8', newline='')
        self.csv_write = csv.DictWriter(self.f, fieldnames=['name', 'title', 'img_url'])
        self.csv_write.writeheader()

    def process_item(self, item, spider):
        # if item not in filter_list:
        #     # 当前这个item是第一次返回的结果
        #     filter_list.append(item)
        #     d = dict(item)
        #     self.csv_write.writerow(d)
        #     return item

        """
        对结果去重的代码
        """
        # d = dict(item)
        # result = hashlib.md5(json.dumps(d).encode()).hexdigest()
        #
        # if result not in filter_list:
        #     # 当前这个item是第一次返回的结果, 就保存到列表中
        #     filter_list.append(result)
        #     self.csv_write.writerow(d)
        #     return item

        d = dict(item)
        self.csv_write.writerow(d)
        return item

    def close_spider(self, spider):
        self.f.close()


"""
缺点: 如果item数据量过多, 数据保存就越慢
"""