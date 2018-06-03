import scrapy
from ..items import ShowinfoItem


class SunZhongShanSpider(scrapy.Spider):
    name = "SunZhongShanSpider"
    start_urls = ['http://www.sunyat-sen.org/']

    def parse(self, response):
        museum = "孙中山故居纪念馆"

        item = ShowinfoItem()

        item['name'] = ""
        item['museum'] = museum
        item['time'] = ""
        item['address'] = ""
        item['introduce'] = ""
        yield item
