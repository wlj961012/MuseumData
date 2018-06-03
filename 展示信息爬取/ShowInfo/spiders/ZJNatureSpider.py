import scrapy
from ..items import ShowinfoItem

class ZJNatureSpider(scrapy.Spider):

    name='ZJNSpider'
    start_urls=['http://www.zmnh.com/exhib_more.php?cat=67']

    def parse(self, response):

        museum='浙江自然博物馆'
        name=response.xpath('//table[@width="723"]//tr[2]/td[2]/a//text()').extract_first()
        time=response.xpath('//table[@width="723"]//tr[2]/td[4]//text()').extract_first()
        address=response.xpath('//table[@width="723"]//tr[2]/td[3]//text()').extract_first()
        page_url=response.xpath('//table[@width="723"]//tr[2]/td[2]/a/@href').extract_first()
        item=ShowinfoItem()
        item['museum']=museum
        item['name']=name
        item['time']=time
        item['address']=address
        page_url='http://www.zmnh.com/'+page_url
        yield scrapy.Request(page_url,callback=self.parse_page,meta=item)

    def parse_page(self,response):
        item=response.meta
        introduce=response.xpath('//td[@class="text"]//text()').extract()
        item['introduce']=''.join(introduce)
        yield item