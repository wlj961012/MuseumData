import scrapy
from ..items import ShowinfoItem

class YunNanSheng(scrapy.Spider):

    name="YunNanSheng"
    start_urls=['http://www.ynbwg.cn/index.html']

    def parse(self,response):

            item=ShowinfoItem()

            museum="云南省博物馆"

            item['name'] = ""
            item['museum'] = museum
            item['time']=""
            item['address']=""
            item['introduce']=""
            yield item
