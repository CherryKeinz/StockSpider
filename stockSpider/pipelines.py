# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class StockspiderPipeline(object):
    def process_item(self, item, spider):
        return item
class JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open('stock.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        print "11111111111111111111111111111111111"
        print type(item)
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()