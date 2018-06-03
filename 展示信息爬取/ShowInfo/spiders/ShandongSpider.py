import scrapy
from ..items import ShowinfoItem

class ShandongSpider(scrapy.Spider):

    name="ShandongSpider"
    start_urls=['http://www.hebeimuseum.org/channels/9.html']

    def parse(self, response):
        item=ShowinfoItem()
        museum="山东博物馆"
        item['museum']=museum
        item['name']=''
        item['time']=''
        item['address']=''
        item['introduce']=''
        yield item