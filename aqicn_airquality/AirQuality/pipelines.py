# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo,time
from scrapy.conf import settings

class AirqualityPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(settings['MONGODB_URI'])
        db = client[settings['MONGODB_DB']]
        self.coll = db[settings['MONGODB_COLL']]

    def process_item(self, item, spider):
        postItem = dict(item)
        self.coll.insert(postItem)  # 向数据库插入一条记录
        return item
