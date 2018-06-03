import scrapy
from ..items import ShowinfoItem

class HebeiSpider(scrapy.Spider):

    name='HebeiSpider'
    start_urls=['http://www.hebeimuseum.org/channels/9.html']

    def parse(self, response):

        names=response.xpath("//div[@class]/ul/li/h4/a/text()").extract()
        page_urls=response.xpath("//div[@class]/ul/li/h4/a/@href").extract()
        times=response.xpath("//span[@class='time']//text()").extract()

        l=len(names)
        museum="河北博物院"

        for i in range(l):

            item=ShowinfoItem()
            name=names[i]
            page_url=page_urls[i]
            time=times[i]
            item['name']=name
            item['time']=time
            item['museum']=museum
            item['address']=museum
            page_url='http://www.hebeimuseum.org'+page_url

            yield scrapy.Request(page_url,callback=self.parse_page,meta=item)

    def parse_page(self,response):

        item=response.meta
        introduce=response.xpath('//div[@class="bd"]//text()').extract()
        item['introduce']=''.join(introduce)

        yield item
