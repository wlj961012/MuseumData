import scrapy
from ..items import ShowinfoItem

class HanHuaSpider(scrapy.Spider):

    name='HanHuaSpider'
    start_urls=['http://nyhhg.com/a/jx/214.html']

    def parse(self, response):

        museum='南阳汉画馆'
        item=ShowinfoItem()
        item['museum']=museum
        name=response.xpath('//div/div[2]/div[2]/div[1]').xpath('string(.)').extract_first()
        item['name']=name
        time=response.xpath('//div/div[2]/div[2]/div[2]').xpath('string(.)').extract_first()
        time=time.replace('浏览： 发布日期：','')
        item['time']=time
        address='南阳汉画馆'
        item['address']=address
        introduce=response.xpath('//div[@class="content"]').xpath('string(.)').extract_first()
        item['introduce']=introduce

        yield item
