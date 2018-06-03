import scrapy
from ..items import ShowinfoItem

class TianjinSpoder(scrapy.Spider):

    name="TianjinSpider"
    start_urls=["http://www.tjbwg.com/ExhibitionList_10410.html"]

    def parse(self,response):

        museum="天津博物馆"
        names=response.xpath('//div[@class="productshow"]/ul/li/a/p/span//text()').extract()
        page_urls=response.xpath("//div[@class='productshow']/ul/li/a/@href").extract()
        l=len(names)

        for i in range(l):
            item=ShowinfoItem()
            item['name']=names[i]
            item['museum']=museum
            page_url='http://www.tjbwg.com/'+page_urls[i]

            yield scrapy.Request(page_url,callback=self.parse_page,meta=item)

    def parse_page(self,response):

        item=response.meta
        info=response.xpath("//div[@class='picshow_right_11']//text()").extract()
        l=len(info)
        item['time']=info[0].replace('\n','').replace('\r','').replace(' ','')
        item['address']=info[1].replace('\n','').replace('\r','').replace(' ','')
        introduce=response.xpath("//div[@class='picshow_right']//text()").extract()
        item['introduce']=''.join(introduce).replace('\n','').replace('\r','').replace(' ','').replace('\xa0','')
        yield item