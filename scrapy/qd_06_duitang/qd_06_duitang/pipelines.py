# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter


# class Qd06DuitangPipeline:
#     def process_item(self, item, spider):
#         return item
from scrapy.pipelines.images import ImagesPipeline  # 导入下载二进制的类功能


class DownLoadPicturePipeline(ImagesPipeline):
    """二进制数据保存"""
    def get_media_requests(self, item, info):
        # 需要把二进制的地址提取出来
        img_url = item['img_url']
        # 构建二进制数据的请求体
        yield scrapy.Request(url=img_url, meta={'img_url': item['img_url']})

    def file_path(self, request, response=None, info=None, *, item=None):
        file_path = request.meta.get('img_url').split('/')[-1]
        all_file_path = './images/' + file_path
        return all_file_path

