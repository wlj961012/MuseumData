import scrapy
from ..items import ShowinfoItem


class GuangXiMinZuSpider(scrapy.Spider):
    name = "GuangXiMinZuSpider"
    start_urls = ['https://baike.baidu.com/item/%E5%B9%BF%E8%A5%BF%E6%B0%91%E6%97%8F%E5%8D%9A%E7%89%A9%E9%A6%86/2825713?fr=aladdin']

    def parse(self, response):
        museum = "广西民族博物馆"

        item = ShowinfoItem()

        item['name'] = ""
        item['museum'] = museum
        item['time'] = ""
        item['address'] = ""
        item['introduce'] = ""
        yield item
