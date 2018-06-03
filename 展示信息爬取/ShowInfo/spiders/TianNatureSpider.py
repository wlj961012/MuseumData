import scrapy
from ..items import ShowinfoItem

class TianNatureSpider(scrapy.Spider):

    name='TianNatureSpider'
    start_urls=['http://www.tjnhm.com/index.php?p=zlxx&c_id=5&lanmu=2']

    def parse(self, response):

        museum="天津自然博物馆"
        names=response.xpath('//div[@class="pro"]/a[2]//text()').extract()
        page_urls=response.xpath('//div[@class="pro"]/a/@href').extract()
        times=response.xpath('//div[@class="pro"]/div//text()').extract()
        l=len(names)

        for i in range(l):
            item=ShowinfoItem()
            name=names[i]
            page_url='http://www.tjnhm.com/'+page_urls[i]
            item['name']=name
            item['museum']=museum
            item['time']=times[i]
            item['address']=museum

            yield scrapy.Request(page_url,callback=self.parse_page,meta=item)

    def parse_page(self,response):

        item=response.meta
        introduce=response.xpath("//p//text()").extract()
        item['introduce']=''.join(introduce).replace('\n','').replace('\r','').replace('\t','').replace('\u3000','').replace(' ','').replace('\xa0','')

        yield item

