import scrapy
from ..items import ShowinfoItem

class HaiNan(scrapy.Spider):

    name="hainanspider"
    start_urls=['http://www.hainanmuseum.org/zlhd/view/?tag_id=2&aid=86']

    def parse(self, response):

        museum='海南省博物馆'
        item=ShowinfoItem()
        item['museum']=museum
        name=response.xpath('//div/div[2]/div[3]/div/div/div[2]//text()').extract_first()
        item['name']=name
        time=response.xpath('//div/div[2]/div[3]/div/div/div[3]/p[6]/span//text()').extract_first()
        item['time']=time
        address=response.xpath('//div/div[2]/div[3]/div/div/div[3]/p[7]/span//text()').extract_first()
        item['address']=address
        introduce=response.xpath('//div/div[2]/div[3]/div/div/div[3]/p//text()').extract()
        introduce=''.join(introduce)
        item['introduce']=introduce

        yield item