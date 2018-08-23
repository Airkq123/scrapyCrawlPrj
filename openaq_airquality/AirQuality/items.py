# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AirqualityItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()
    date = scrapy.Field()
    query_time = scrapy.Field()
    crawl_time = scrapy.Field()
    lat = scrapy.Field()
    lon = scrapy.Field()
    location = scrapy.Field()
    parameter = scrapy.Field()
    value = scrapy.Field()
    unit = scrapy.Field()

