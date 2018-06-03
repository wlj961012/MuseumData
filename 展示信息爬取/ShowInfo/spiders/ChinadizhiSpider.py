import scrapy
from ..items import ShowinfoItem

class DizhiSpider(scrapy.Spider):

    name='dizhiSpider'
    start_urls=['http://www.gmc.org.cn/hall/132']

    def parse(self,response):

        museum='中国地质博物馆'
        item=ShowinfoItem()
        item['name']=''
        item['time']=''
        item['address']=''
        item['introduce']=''
        item['museum']=museum
        yield item