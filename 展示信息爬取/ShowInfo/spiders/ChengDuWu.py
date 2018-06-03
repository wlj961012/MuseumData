import scrapy
from ..items import ShowinfoItem

class ZiGongSpider(scrapy.Spider):

    name="ChenDuHouSpider"
    start_urls=['https://lvyou.baidu.com/wuhouci/']

    def parse(self,response):

            item=ShowinfoItem()

            museum="成都武侯祠博物馆"

            item['name'] = ""
            item['museum'] = museum
            item['time']=""
            item['address']=""
            item['introduce']=""
            yield item
