import scrapy
from ..items import ShowinfoItem

class ZhengZhouSpider(scrapy.Spider):

    name='ZhengZhouSpider'
    start_urls=['http://www.hnzzmuseum.com/showzl.asp?uid=48']

    def parse(self, response):

        museum='郑州博物馆'
        item=ShowinfoItem()

        time=response.xpath('//div/div[2]/div[2]/p[1]//text()').extract_first()
        name=response.xpath('//ul[@class="news_title"]//text()').extract_first()
        address=response.xpath('//div/div[2]/div[2]/p[3]//text()').extract_first()
        introduce=response.xpath('//div/div[2]/div[2]/ul[2]').xpath('string(.)').extract_first()
        item['museum']=museum
        item['time']=time
        item['name']=name
        item['address']=address
        item['introduce']=introduce

        yield item



