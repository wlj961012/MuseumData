import scrapy
from ..items import ShowinfoItem

class BeijingSpider(scrapy.Spider):

    name="BeijingSpider"
    start_urls=['http://www.capitalmuseum.org.cn/zlxx/zxzl.htm']

    def parse(self, response):

        museum="首都博物馆"
        content=response.xpath('//td[@height="72"]//text()').extract()
        l=len(content)

        for i in range(0,l,4):
            j=i
            item=ShowinfoItem()
            time=content[j]
            address=content[j+2]
            name=response.xpath("//a[@class='btitle']//text()").extract_first()
            item['name']=name
            item['museum']=museum
            item['time']=time
            item['address']=address
            page_url=response.xpath('//a[@class="hh"]/@href').extract_first()

            if page_url:
                page_url='http://www.capitalmuseum.org.cn/zlxx/'+page_url
                yield scrapy.Request(page_url,callback=self.parse_page,meta=item)

    def parse_page(self,response):

        item=response.meta
        content=response.xpath("//table[@width='600']//text()").extract()
        item['introduce']=''.join(content).replace('\n','').replace('\t','').replace('\r','').replace('\xa0','').replace(' ','')

        yield item


            

