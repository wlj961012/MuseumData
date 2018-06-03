import scrapy
from ..items import ShowinfoItem

class SuZhouSpider(scrapy.Spider):

    name="SuZhouSpider"
    start_urls=['http://www.szmuseum.com/Exhibition/TemporaryDetails/9a4427dc-eb7d-4ec0-99d6-f5342953c2d2?startYear=2018-04-28']

    def parse(self, response):
        item=ShowinfoItem()

        museum="苏州博物馆"

        name=response.xpath("//div/div[3]/div/h1//text()").extract()[0]

        time=response.xpath("//div/div[3]/div/div[1]/span[1]//text()").extract()[0]
        address=response.xpath("//div/div[3]/div/div[1]/span[2]//text()").extract()[0]
        introduce=response.xpath("//div/div[3]/div/div[2]/p[40]//text()").extract()[0]

        item['name'] =name
        item['museum'] = museum
        item['time']=time
        item['address']=address
        item['introduce']=introduce
        yield item
