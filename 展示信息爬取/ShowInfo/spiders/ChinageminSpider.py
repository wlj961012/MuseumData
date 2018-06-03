import scrapy
from ..items import ShowinfoItem

class ChinageminSpider(scrapy.Spider):

    name='GeminSpider'
    start_urls=['http://www.jb.mil.cn/zlcl/jbcl/']

    def parse(self, response):

        museum='中国人民革命军事博物馆'
        item=ShowinfoItem()
        item['name']=''
        item['time']=''
        item['address']=''
        item['introduce']=''
        item['museum']=museum
        yield item