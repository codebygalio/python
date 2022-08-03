# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CsvPipeline:
    def process_item(self, item, spider):
        # item 会拿到爬虫文件返回的所有条数据
        d = dict(item)

        with open('zhangzishi.csv', mode='a', encoding='utf-8') as f:
            f.write(d['title'] + ',' + d['info'] + d['reads'] + d['commons'])
            f.write('\n')

        return item
