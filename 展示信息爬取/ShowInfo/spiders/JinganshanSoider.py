import scrapy
from ..items import ShowinfoItem

class JinGangshanSpider(scrapy.Spider):

    name="JingangshanSpider"
    start_urls=['http://www.hebeimuseum.org/channels/9.html']

    def parse(self, response):
        item=ShowinfoItem()
        museum="井冈山革命博物馆"
        item['museum']=museum
        item['name']=''
        item['time']=''
        item['address']=''
        item['introduce']=''
        yield item