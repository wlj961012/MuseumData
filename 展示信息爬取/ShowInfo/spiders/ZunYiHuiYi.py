import scrapy
from ..items import ShowinfoItem

class ZunYiHuiYi(scrapy.Spider):

    name="ZunYiHuiYi"
    start_urls=['http://www.zunyihy.cn/index.html']

    def parse(self,response):

            item=ShowinfoItem()

            museum="遵义会议纪念馆"

            item['name'] = ""
            item['museum'] = museum
            item['time']=""
            item['address']=""
            item['introduce']=""
            yield item
