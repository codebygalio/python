# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# class Qd03EnglishPipeline:
#     def process_item(self, item, spider):
#         # item 返回的就是一个字典对象
#         with open('english.csv', mode='a', encoding='utf-8') as f:
#             f.write(item['title'] + "," + item['info'] + "," + item['img_url'] + '\n')
#         return item
import csv
import json


class CsvPipeline:
    def __init__(self):
        """初始化方法, 一般打开文件, 建立数据连接"""
        self.f = open('english.csv', mode='a', encoding='utf-8', newline='')
        self.csv_write = csv.DictWriter(self.f, fieldnames=['title', 'info', 'img_url'])
        # 写入表头, 只需要写入一次
        self.csv_write.writeheader()

    def process_item(self, item, spider):
        """
        process_item 专门处理item数据结构返回的数据
        :param item: items.py 数据结构返回的一条一条的数据
        :param spider: 爬虫对象
        :return: item数据结构的数据必须原路返回
        """
        d = dict(item)
        self.csv_write.writerow(d)

        # item必须原路返回
        # 因为可能不只有一个Pipeline的管道类
        return item

    def close_spider(self, spider):
        """整个scrapy的项目在停止之前会调用的方法, 一般用于关闭文件或者数据库的连接"""
        self.f.close()

"""
[{}, {}, {}..]
{字段1:{值: 值1}....}
"""
class JsonPipeline:
    def open_spider(self, spider):
        self.f = open('english.json', mode='w', encoding='utf-8')
        # 收集每一条 item 返回的数据
        self.data_list = []

    def process_item(self, item, spider):
        d = dict(item)
        self.data_list.append(d)
        return item

    def close_spider(self, spider):
        # 序列化json数据
        json_data = json.dumps(self.data_list, ensure_ascii=False)
        self.f.write(json_data)
        self.f.close()


"""
....
"""