import scrapy
from ..items import ShowinfoItem

class ShenYangGuGongSpider(scrapy.Spider):

    name="shenyanggugongSpider"
    start_urls=['http://www.nmgbwy.com/zldt/1356.jhtml']

    def parse(self, response):

        museum="沈阳故宫博物院"

        name=response.xpath("//div/div[2]/div[4]/div/div/div/font//text()").extract()[0]
        item=ShowinfoItem()

        time=response.xpath("//div/div[2]/div[4]/div/div/p[6]//text()").extract()[1]
        address=response.xpath("//div/div[2]/div[4]/div/div/p[7]//text()").extract()[1]
        introduce=response.xpath("//div/div[2]/div[4]/div/div/p[8]//text()").extract()[0]

        item['name'] =""
        item['museum'] = museum
        item['time']=""
        item['address']=""
        item['introduce']=""
        yield item
