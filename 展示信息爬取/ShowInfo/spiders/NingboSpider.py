import scrapy
from ..items import ShowinfoItem

class NingboSpider(scrapy.Spider):

    name='Ningbospider'
    start_urls=['http://www.nbmuseum.cn/art/2018/4/23/art_461_661.html']

    def parse(self,response):

        name='甬上留香——弘一法师翰墨展'
        time='2018.04.28-2018.05.27'
        address='宁波博物馆一楼东特展馆'
        museum='宁波博物馆'
        item=ShowinfoItem()
        item['name']=name
        item['time']=time
        item['address']=address
        item['museum']=museum
        introduce=response.xpath('//div/div[2]/div[2]/div[2]/div[2]//text()').extract()
        item['introduce']=''.join(introduce)
        yield item