import scrapy
from ..items import ShowinfoItem

class MinxiSpider(scrapy.Spider):

    name="minxiSpider"
    start_urls=['http://www.hebeimuseum.org/channels/9.html']

    def parse(self, response):
        item=ShowinfoItem()
        museum="中央苏区(闽西)历史博物馆"
        item['museum']=museum
        item['name']=''
        item['time']=''
        item['address']=''
        item['introduce']=''
        yield item
