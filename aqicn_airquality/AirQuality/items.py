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
    crawl_time = scrapy.Field()
    query_time = scrapy.Field()
    aq_unit = scrapy.Field()
    min_PM25 = scrapy.Field()
    max_PM25 = scrapy.Field()
    min_PM10 = scrapy.Field()
    max_PM10 = scrapy.Field()
    min_O3 = scrapy.Field()
    max_O3 = scrapy.Field()
    min_NO2 = scrapy.Field()
    max_NO2 = scrapy.Field()
    min_SO2 = scrapy.Field()
    max_SO2 = scrapy.Field()
    min_CO = scrapy.Field()
    max_CO = scrapy.Field()
    temp_unit = scrapy.Field()
    min_Temp = scrapy.Field()
    max_Temp = scrapy.Field()
    dew_unit = scrapy.Field()
    min_Dew = scrapy.Field()
    max_Dew = scrapy.Field()
    pressure_unit = scrapy.Field()
    min_Pressure = scrapy.Field()
    max_Pressure = scrapy.Field()
    min_Humidity = scrapy.Field()
    max_Humidity = scrapy.Field()
    wind_unit = scrapy.Field()
    min_wind = scrapy.Field()
    max_wind = scrapy.Field()

