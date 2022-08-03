# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv

import scrapy
from itemadapter import ItemAdapter


# class Qd07Win4000Pipeline:
#     def process_item(self, item, spider):
#         return item
from scrapy.pipelines.images import ImagesPipeline


class CsvPipeline:
    def __init__(self):
        self.f = open('图片.csv', mode='a', encoding='utf-8', newline='')
        self.csv_write = csv.DictWriter(self.f, fieldnames=['title', 'urls'])
        self.csv_write.writeheader()

    def process_item(self, item, spider):
        d = dict(item)
        self.csv_write.writerow(d)
        return item

    def close_spider(self, spider):
        self.f.close()


class DownloadPicturePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        """把图片的下载地址构建成一个requests请求"""
        for url in item['urls']:
            # 构建一个请求之前, 如果有 file_path 函数, 会被这个函数预先处理
            yield scrapy.Request(url, meta={'title': item['title']})

    def file_path(self, request, response=None, info=None, *, item=None):
        """
        指定文件保存的路径
        :param request:
        :return: 文件路径
        """
        # 获取item里面图片系列的名字
        dir_name = request.meta.get('title')
        # 通过split分割, 取出图片的名字
        file_name = request.url.split('/')[-1]
        # return 返回文件路径
        return dir_name + '\\' + file_name

