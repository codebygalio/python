# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

"""
数据管道: (所有的数据都会流经数据管道)
    一般用于数据持久化操作
"""


class Qd01QuotesPipeline:
    def process_item(self, item, spider):
        # item 会拿到爬虫文件返回的所有条数据
        d = dict(item)

        with open('quotes.csv', mode='a', encoding='utf-8') as f:
            f.write(d['text'] + ',' + d['author'] + ',' + '/'.join(d['tags']))
            f.write('\n')
        return item

"""
管道逻辑写完以后, 一定要注意需要在配置文件进行配置
"""
