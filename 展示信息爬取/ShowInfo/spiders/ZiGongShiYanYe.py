import scrapy
from ..items import ShowinfoItem

class ZiGongShiYanYe(scrapy.Spider):

    name="ZiGongShiYanYe"
    start_urls=['https://baike.baidu.com/item/%E8%87%AA%E8%B4%A1%E5%B8%82%E7%9B%90%E4%B8%9A%E5%8E%86%E5%8F%B2%E5%8D%9A%E7%89%A9%E9%A6%86/2035378?fr=aladdin']

    def parse(self,response):

            item=ShowinfoItem()

            museum="自贡市盐业历史博物馆"

            item['name'] = ""
            item['museum'] = museum
            item['time']=""
            item['address']=""
            item['introduce']=""
            yield item
