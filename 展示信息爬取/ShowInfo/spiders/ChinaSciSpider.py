import scrapy
from ..items import ShowinfoItem

class ChinasciSpider(scrapy.Spider):

    name="ChinasciSpider"
    start_urls=['http://cstm.cdstm.cn/e/action/ListInfo/?classid=310']

    def parse(self, response):

        name=response.xpath('//div/div[3]/div[2]/h2//text()').extract_first()
        introduce=response.xpath('//div/div[3]/div[2]/p[4]//text()').extract_first()
        time=response.xpath('//div/div[3]/div[2]/p[5]//text()').extract()[-1]
        address=response.xpath('//div/div[3]/div[2]/p[6]//text()').extract()[-1]
        item=ShowinfoItem()
        museum='中国科学技术馆'
        item['museum']=museum
        item['name']=name
        item['introduce']=introduce
        item['time']=time
        item['address']=address
        yield item