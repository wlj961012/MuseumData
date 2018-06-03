import scrapy
from ..items import ShowinfoItem

class ChengDuDuFu(scrapy.Spider):

    name="ChengDuDuFu"
    start_urls=['https://baike.baidu.com/item/%E6%88%90%E9%83%BD%E6%9D%9C%E7%94%AB%E8%8D%89%E5%A0%82%E5%8D%9A%E7%89%A9%E9%A6%86/4824775?fr=aladdin']

    def parse(self,response):

            item=ShowinfoItem()

            museum="成都杜甫草堂博物馆"

            item['name'] = ""
            item['museum'] = museum
            item['time']=""
            item['address']=""
            item['introduce']=""
            yield item