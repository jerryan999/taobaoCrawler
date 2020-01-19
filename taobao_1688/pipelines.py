# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.utils.project import get_project_settings

settings = get_project_settings()


class Taobao1688Pipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection_detail = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        self.collection_detail.update({'url':item['url']},item,True)
        return item
