from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector
from ..items import AirqualityItem
import scrapy,json,time,re

class AirQualityOpenaqspider(CrawlSpider):
    name = 'AQ'
    query_time = str(time.strftime("%Y-%m-%d,%H:%M:%S", time.localtime()))
    cities = ["Bengbu","Tongling","Suzhou","Huaibei","Fuyang","Shanghai","Wuhu","Hefei","Ma'anshan","Huainan"
        ,"Lu'an","Bozhou","Chizhou","Chengdu","Xuancheng","Chuzhou","Huangshan","Beijing","Anqing","Guangzhou","Shenyang"]
    def start_requests(self):
        d = time.strftime('%Y-%m-%d',time.gmtime())
        t1 = time.strftime('%H:%M:%S',time.gmtime(time.time()-9000))
        t2 = time.strftime('%H:%M:%S',time.gmtime(time.time()-5400))
        for i in self.cities:
            url = "https://api.openaq.org/v1/measurements?city={0}&date_from={1}T{2}&date_to={1}T{3}".format(i,d,t1,t2)
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self, response):
        item = AirqualityItem()
        results = json.loads(response.body.decode(response.encoding))['results']
        for result in results:
            item['city'] = result['city']
            s = result['date']['local'][:-6]
            item['date'] = re.sub('T',',',s)
            item['query_time'] = self.query_time
            item['crawl_time'] = str(time.strftime("%Y-%m-%d,%H:%M:%S", time.localtime()))
            item['lat'] = result['coordinates']['latitude']
            item['lon'] = result['coordinates']['longitude']
            item['location'] = result['location']
            item['parameter'] = result['parameter']
            item['value'] = result['value']
            item['unit'] = result['unit']
            yield item