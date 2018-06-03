import scrapy
from ..items import ShowinfoItem

class ZiGongSpider(scrapy.Spider):

    name="ZiGongSpider"
    start_urls=['http://www.zdm.cn/']

    def parse(self,response):

            item=ShowinfoItem()

            museum="自贡恐龙博物馆"

            item['name'] = ""
            item['museum'] = museum
            item['time']=""
            item['address']=""
            item['introduce']=""
            yield item
