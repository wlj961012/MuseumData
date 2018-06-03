import scrapy
from ..items import ShowinfoItem

class HongyanSpider(scrapy.Spider):

    name="HongyanSpider"
    start_urls=['http://www.hongyan.info/']

    def parse(self, response):
        item=ShowinfoItem()

        museum="重庆红岩革命历史博物馆"
        item['museum'] = museum
        item['name'] = ''
        item['time'] = ''
        item['address'] = ''
        item['introduce'] = ''

        yield item