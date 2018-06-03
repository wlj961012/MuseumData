import scrapy
from ..items import ShowinfoItem

class ShanxiSpider(scrapy.Spider):

    name="ShanxiSpider"
    start_urls=['http://www.shanximuseum.com/exhibition/current.html']

    def parse(self, response):

        museum='山西博物院'
        names=response.xpath("//div[@class='cbox rdshow']/div/dl/dd/strong//text()").extract()
        page_urls=response.xpath("//div[@class='cbox rdshow']/div/dl/dt/a/@href").extract()

        l=len(names)

        for i in range(l):
            item=ShowinfoItem()
            item['name']=names[i]
            item['museum']=museum
            page_url='http://www.shanximuseum.com'+page_urls[i]
            yield scrapy.Request(page_url,callback=self.parse_page,meta=item)

    def parse_page(self,response):

        item=response.meta
        content=response.xpath("//div[@class='cboxs cContainer']/div/div[1]//text()").extract()
        item['time']=content[0]
        item['address']=content[-1]
        introduce=response.xpath("//div[@class='cboxs cContainer']/div/div[2]//text()").extract()
        item['introduce']=''.join(introduce)
        yield item