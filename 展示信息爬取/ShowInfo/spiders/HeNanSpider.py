import scrapy
from ..items import ShowinfoItem

class HeNanSpider(scrapy.Spider):

    name='HeNanSpider'
    start_urls=['http://www.chnmus.net/clzl/201802/07/content_411373.htm']

    def parse(self, response):

        museum='河南博物院'
        item=ShowinfoItem()
        item['museum']=museum
        name=response.xpath('//td[@id="wzbt"]//text()').extract_first()
        item['name']=name
        introduce=response.xpath('//*[@id="Zoom"]').xpath('string(.)').extract_first()
        item['introduce']=introduce
        address=museum
        item['address']=address
        time=response.xpath('//table/tr[2]/td[2]/article/table/tr[4]/td//text()').extract_first()
        item['time']=time
        yield item