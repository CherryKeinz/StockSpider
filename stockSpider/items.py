# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StockspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class stockItem(scrapy.Item):
    id = scrapy.Field()
    symbol = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    change = scrapy.Field()
    chg = scrapy.Field()
    amplitude = scrapy.Field()
    volume =scrapy.Field()
    turnover =scrapy.Field()
    preclose = scrapy.Field()
    open = scrapy.Field()
    higheset = scrapy.Field()
    loweset = scrapy.Field()
    changeinfive = scrapy.Field()

