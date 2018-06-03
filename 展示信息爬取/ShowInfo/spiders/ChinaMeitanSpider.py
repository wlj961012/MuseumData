import scrapy
from ..items import ShowinfoItem

class ChinaMeitanSpider(scrapy.Spider):

    name="meitanSpider"
    start_urls=['http://www.coalmus.org.cn/html/list_1659.html']

    def parse(self, response):

        museum="中国煤炭博物馆"
        names=response.xpath("//div[@id='LB']/ul/li/h2/a/text()").extract()
        page_urls=response.xpath("//div[@id='LB']/ul/li/h2/a/@href").extract()
        l=len(names)

        for i in range(l):
            item=ShowinfoItem()
            item['name']=names[i]
            item['museum']=museum
            page_url=page_urls[i]
            yield scrapy.Request(page_url,callback=self.parse_page,meta=item)

    def parse_page(self,response):

        item=response.meta
        time=response.xpath("//div[@id='MyContent']/p[2]/text()").extract()
        address=response.xpath("//div[@id='MyContent']/p[3]/text()").extract()
        time=''.join(time)
        address=''.join(address)
        introduce=response.xpath("//div[@id='MyContent']").xpath('string(.)').extract()
        introduce=''.join(introduce).replace(time,'').replace(address,'')
        item['time']=time
        item['address']=address
        item['introduce']=introduce
        yield item