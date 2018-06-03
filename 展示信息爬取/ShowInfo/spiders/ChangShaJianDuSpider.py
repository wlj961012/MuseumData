import scrapy
from ..items import ShowinfoItem


class ChangShaJianDuSpider(scrapy.Spider):
    name = "ChangShaJianDuSpider"
    start_urls = ['http://jdbwg.360500.com/']

    def parse(self, response):
        museum = "长沙简牍博物馆"

        item = ShowinfoItem()

        item['name'] = ""
        item['museum'] = museum
        item['time'] = ""
        item['address'] = ""
        item['introduce'] = ""
        yield item