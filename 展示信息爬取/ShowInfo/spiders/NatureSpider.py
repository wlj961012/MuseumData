import scrapy
from ..items import ShowinfoItem

class NatureSpider(scrapy.Spider):

    name='NatureSpider'
    start_urls=['http://www.bmnh.org.cn/Html/List/list10.html']

    def parse(self,reponse):

        museum='北京自然博物馆'
        item=ShowinfoItem()

        content=reponse.xpath("//div[@class='show-column']")

        for i in content:
            names=i.xpath("//ul/li/b/a//text()").extract()
            times=i.xpath("//ul/li/em/text()").extract()
            page_urls=i.xpath("//ul/li/b/a/@href").extract()
            l=len(names)
            for j in range(l):
                item=ShowinfoItem()
                item['name']=names[j]
                item['time']=times[j]
                item['museum']=museum
                item['address']=museum
                if page_urls[j]:
                    page_url='http://www.bmnh.org.cn/'+page_urls[j]
                    yield scrapy.Request(page_url,callback=self.parse_page,meta=item)

    def parse_page(self,response):
        item=response.meta
        content=response.xpath('//div[@class="zoom"]//text()').extract()
        content=''.join(content).replace(' ','').replace('\n','').replace('\r','').replace('\xa0','').replace('\u3000e','')
        item['introduce']=content
        #item['address']=content
        yield item
