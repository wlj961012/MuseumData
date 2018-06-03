import scrapy
from ..items import ShowinfoItem

class DengXiaoPing(scrapy.Spider):

    name="DengXiaoPing"
    start_urls=['https://baike.baidu.com/item/%E9%82%93%E5%B0%8F%E5%B9%B3%E6%95%85%E5%B1%85%E9%99%88%E5%88%97%E9%A6%86/9803788']

    def parse(self,response):

            item=ShowinfoItem()

            museum="邓小平故居陈列馆"

            item['name'] = ""
            item['museum'] = museum
            item['time']=""
            item['address']=""
            item['introduce']=""
            yield item