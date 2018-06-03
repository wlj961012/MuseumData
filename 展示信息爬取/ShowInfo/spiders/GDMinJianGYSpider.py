import scrapy
from ..items import ShowinfoItem


class GDMinJianGYSpider(scrapy.Spider):
    name = "GDMinJianGYSpider"
    start_urls = ['https://baike.baidu.com/item/%E5%B9%BF%E4%B8%9C%E6%B0%91%E9%97%B4%E5%B7%A5%E8%89%BA%E5%8D%9A%E7%89%A9%E9%A6%86/1627374?fr=aladdin']

    def parse(self, response):
        museum = "广东民间工艺博物馆"

        item = ShowinfoItem()

        item['name'] = ""
        item['museum'] = museum
        item['time'] = ""
        item['address'] = ""
        item['introduce'] = ""
        yield item
