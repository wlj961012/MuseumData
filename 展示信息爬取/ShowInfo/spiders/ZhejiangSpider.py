import scrapy
from ..items import ShowinfoItem

class ZhejiangSpider(scrapy.Spider):

    name='zhejiangSpider'
    start_urls=['http://www.zhejiangmuseum.com/zjbwg/exhibition/exhcurrent.html']

    def parse(self, response):

        names=response.xpath('//ul[@class="zanlan_list"]/li/div/h4/a//text()').extract()
        page_urls=response.xpath('//ul[@class="zanlan_list"]/li/div/h4/a/@href').extract()
        times=response.xpath('//div[@class="list_left"]//text()').extract()
        addresss=response.xpath('//div[@class="list_right"]//text()').extract()
        l=len(names)
        museum='浙江省博物馆'

        for i in range(l):
            item=ShowinfoItem()
            item['name']=names[i]
            item['time']=times[i*3+2]
            item['address']=addresss[i*3+2]
            item['museum']=museum
            page_url='http://www.zhejiangmuseum.com/zjbwg/exhibition/'+page_urls[i]
            yield scrapy.Request(page_url,callback=self.parse_page,meta=item)

    def parse_page(self,response):

        item=response.meta
        introduce=response.xpath('//div[@class="zanlan_zs"]').xpath('string(.)').extract()
        item['introduce']=''.join(introduce)
        yield item