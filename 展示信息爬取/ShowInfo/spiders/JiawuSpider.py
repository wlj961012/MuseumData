import scrapy
from ..items import ShowinfoItem

class JiawuSpider(scrapy.Spider):

    name="JiawuSpider"
    start_urls=['http://www.hebeimuseum.org/channels/9.html']

    def parse(self, response):
        item=ShowinfoItem()
        museum="中国甲午战争博物馆"
        item['museum']=museum
        item['name']=''
        item['time']=''
        item['address']=''
        item['introduce']=''
        yield item