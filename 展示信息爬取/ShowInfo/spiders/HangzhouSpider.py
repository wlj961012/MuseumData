import scrapy
from ..items import ShowinfoItem

class HangzhouSpider(scrapy.Spider):

    name='HZSpider'
    start_urls=['http://www.hzmuseum.com/exhibition.aspx?cid=12']

    def parse(self, response):
        name=response.xpath('//div[@class="div2 rg"]/p[1]/a//text()').extract_first()
        time=response.xpath('//div[@class="div2 rg"]/p[3]//text()').extract_first()
        address=response.xpath('//div[@class="div2 rg"]/p[4]//text()').extract_first()
        museum='杭州博物馆'
        item=ShowinfoItem()
        item['name']=name
        item['time']=time
        item['address']=address
        item['museum']=museum
        page_url=response.xpath('//div[@class="div2 rg"]/p[1]/a/@href').extract_first()
        page_url='http://www.hzmuseum.com/'+page_url
        yield scrapy.Request(page_url,callback=self.parse_page,meta=item)

    def parse_page(self,response):
        item=response.meta
        introduce=response.xpath("//p").xpath('string(.)').extract()
        item['introduce']=''.join(introduce)
        yield item