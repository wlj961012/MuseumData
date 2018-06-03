import scrapy
from ..items import ShowinfoItem

class SiChuan(scrapy.Spider):

    name="SiChuan"
    start_urls=['https://baike.baidu.com/item/%E5%9B%9B%E5%B7%9D%E5%8D%9A%E7%89%A9%E9%99%A2/2812558?fr=aladdin']

    def parse(self,response):

            item=ShowinfoItem()

            museum="四川博物馆"

            item['name'] = ""
            item['museum'] = museum
            item['time']=""
            item['address']=""
            item['introduce']=""
            yield item
