import scrapy
from ..items import ShowinfoItem

class GutianSpider(scrapy.Spider):

    name="GutianSpider"
    start_urls=['http://www.hebeimuseum.org/channels/9.html']

    def parse(self, response):
        item=ShowinfoItem()
        museum="古田会议纪念馆"
        item['museum']=museum
        item['name']=''
        item['time']=''
        item['address']=''
        item['introduce']=''
        yield item