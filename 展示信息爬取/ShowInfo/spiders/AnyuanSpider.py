import scrapy
from ..items import ShowinfoItem

class AnyuanSpider(scrapy.Spider):

    name="AnyuanSpider"
    start_urls=['http://www.hebeimuseum.org/channels/9.html']

    def parse(self, response):
        item=ShowinfoItem()
        museum="安源路矿工人运动纪念馆"
        item['museum']=museum
        item['name']=''
        item['time']=''
        item['address']=''
        item['introduce']=''
        yield item