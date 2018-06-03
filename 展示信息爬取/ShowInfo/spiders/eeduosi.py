import scrapy
from ..items import ShowinfoItem

class eeduosiSpider(scrapy.Spider):

    name="eeduosiSpiider"
    start_urls=['http://www.nmgbwy.com/zldt/1356.jhtml']

    def parse(self, response):

        museum="鄂尔多斯博物馆"
        
        item=ShowinfoItem()

        item['name'] = ""
        item['museum'] = museum
        item['time']=""
        item['address']=""
        item['introduce']=""
        yield item
