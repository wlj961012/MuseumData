import scrapy
from ..items import ShowinfoItem

class ChinaSpider(scrapy.Spider):

    name="ChinaSpider"
    start_urls=["http://www.chnmuseum.cn/tabid/304/Default.aspx"]

    def parse(self, response):

        museum="中国国家博物馆"
        names=response.xpath("//td[@valign='top']/li/span[1]//text()").extract()
        times=response.xpath("//td[@valign='top']/li/span[2]/span//text()").extract()
        addresss=response.xpath("//td[@valign='top']/li/span[3]/span//text()").extract()
        page_urls=response.xpath("//td[@valign='top']/li/a/@href").extract()
        l=len(names)

        for i in range(l):
            item=ShowinfoItem()
            item['name']=names[i]
            item['time']=times[i]
            item['address']=addresss[i]
            item['museum']=museum
            page_url='http://www.chnmuseum.cn/'+page_urls[i]
            yield scrapy.Request(page_url,callback=self.parse_page,meta=item)

    def parse_page(self,response):

        item=response.meta
        content=response.xpath("//p").xpath('string(.)').extract()
        content = ''.join(content).replace(' ', '').replace('\n', '').replace('\r', '').replace('\xa0', '').replace('\u3000e', '')
        if content:
            item['introduce']=content
            yield item