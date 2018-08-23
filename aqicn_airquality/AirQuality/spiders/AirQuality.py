from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector
from ..items import AirqualityItem
import scrapy,json,time

class AirQualityAqispider(CrawlSpider):
    name = 'AQ2'
    f = open('AirQuality/cities.txt','r+')
    query_time = str(time.strftime("%Y-%m-%d,%H:%M:%S", time.localtime()))
    cities = []
    for i in range(3, 233):
        cities.append(f.readline()[:-1])
    f.close()
    def start_requests(self):
        for j in self.cities:
            url = 'http://aqicn.org/city/'+j+'/'
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self, response):
        item = AirqualityItem()
        selector = Selector(response)
        item['city'] = selector.xpath('//*[@id="city0"]/span[1]/text()').extract_first()
        item['date'] = selector.xpath('//*[@id="aqiwgtutime"]/text()').extract_first()[11:]
        item['crawl_time'] = str(time.strftime("%Y-%m-%d,%H:%M:%S", time.localtime()))
        item['query_time'] = self.query_time
        item['aq_unit'] = 'ug/m3'
        item['min_PM25'] = selector.xpath('//*[@id="min_pm25"]/text()').extract_first()
        item['max_PM25'] = selector.xpath('//*[@id="max_pm25"]/text()').extract_first()
        item['min_PM10'] = selector.xpath('//*[@id="min_pm10"]/text()').extract_first()
        item['max_PM10'] = selector.xpath('//*[@id="max_pm10"]/text()').extract_first()
        item['min_O3'] = selector.xpath('//*[@id="min_o3"]/text()').extract_first()
        item['max_O3'] = selector.xpath('//*[@id="max_o3"]/text()').extract_first()
        item['min_NO2'] = selector.xpath('//*[@id="min_no2"]/text()').extract_first()
        item['max_NO2'] = selector.xpath('//*[@id="max_no2"]/text()').extract_first()
        item['min_SO2'] = selector.xpath('//*[@id="min_so2"]/text()').extract_first()
        item['max_SO2'] = selector.xpath('//*[@id="max_so2"]/text()').extract_first()
        item['min_CO'] = selector.xpath('//*[@id="min_co"]/text()').extract_first()
        item['max_CO'] = selector.xpath('//*[@id="max_co"]/text()').extract_first()
        item['temp_unit'] = '℃'
        item['min_Temp'] = selector.xpath('//*[@id="min_t"]/span/text()').extract_first()
        item['max_Temp'] = selector.xpath('//*[@id="max_t"]/span/text()').extract_first()
        item['dew_unit'] = '℉'
        item['min_Dew'] = selector.xpath('//*[@id="min_d"]/span/text()').extract_first()
        item['max_Dew'] = selector.xpath('//*[@id="max_d"]/span/text()').extract_first()
        item['pressure_unit'] = 'mbar'
        item['min_Pressure'] = selector.xpath('//*[@id="min_p"]/text()').extract_first()
        item['max_Pressure'] = selector.xpath('//*[@id="max_p"]/text()').extract_first()
        item['min_Humidity'] = selector.xpath('//*[@id="min_h"]/text()').extract_first()
        item['max_Humidity'] = selector.xpath('//*[@id="max_h"]/text()').extract_first()
        item['wind_unit'] = 'm/s'
        item['min_wind'] = selector.xpath('//*[@id="min_w"]/text()').extract_first()
        item['max_wind'] = selector.xpath('//*[@id="max_w"]/text()').extract_first()
        yield item