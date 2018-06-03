import scrapy
from ..items import ShowinfoItem

class BaluSpider(scrapy.Spider):

    name="BaluSpider"
    start_urls=['http://www.hebeimuseum.org/channels/9.html']

    def parse(self, response):
        item=ShowinfoItem()
        museum="八路军太行纪念馆"
        item['museum']=museum
        item['name']=''
        item['time']=''
        item['address']=''
        item['introduce']=''
        yield item