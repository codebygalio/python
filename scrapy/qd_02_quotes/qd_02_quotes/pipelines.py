# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from itemadapter import ItemAdapter
import csv


class Qd02QuotesPipeline:
    def process_item(self, item, spider):
        return item


class CsvPipeline(object):
    def __init__(self):
        """类初始化操作, 打开文件的业务逻辑"""
        self.file = open('data.csv', mode='a', encoding='utf-8', newline='')
        self.csv_write = csv.DictWriter(self.file, fieldnames=['text', 'author', 'tags'])
        self.csv_write.writeheader()

    # def open_spider(self, spider):
    #     ## spider (Spider 对象) – 被开启的spider
    #     ## 可选实现，当spider被开启时，这个方法被调用。
    #     pass

    def process_item(self, item, spider):
        """

        :param item: spider中返回的数据结构
        :param spider: 爬虫对象
        :return: 用完之后, 返回交给下一个管道文件保存
        """
        ## item (Item 对象) – 被爬取的item
        ## spider (Spider 对象) – 爬取该item的spider
        ## 这个方法必须实现，每个item pipeline 组件都需要调用该方法，
        ## 这个方法必须返回一个 Item 对象，被丢弃的item将不会被之后的pipeline组件所处理。

        d = dict(item)
        self.csv_write.writerow(d)
        return item

    def close_spider(self, spider):
        ## spider (Spider 对象) – 被关闭的spider
        ## 可选实现，当spider被关闭时，这个方法被调用
        self.file.close()


class JsonPipeline(object):
    def __init__(self):
        self.file = open('data.json', mode='w', encoding='utf-8', newline='')
        # 手机每一条item数据
        self.d_list = []

    def process_item(self, item, spider):
        d = dict(item)
        self.d_list.append(d)
        return item

    def close_spider(self, spider):
        """scrapy项目停止前会调用的一个方法"""
        self.file.write(json.dumps(self.d_list, ensure_ascii=False))
        self.file.close()