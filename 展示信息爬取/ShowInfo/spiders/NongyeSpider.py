import scrapy
from ..items import ShowinfoItem

class NongyeSpider(scrapy.Spider):

    name="NongyeSpider"
    start_urls=['http://www.zgnybwg.com.cn/list/zh/political.html']

    def parse(self,response):

        museum="中国农业博物馆"
        names=response.xpath("//div/div/div/div/ul/li/a/div[2]/h3//text()").extract()
        page_urls=response.xpath("//div/div/div/div/ul/li/a/@href").extract()
        l = len(names)

        for i in range(l):
            item=ShowinfoItem()
            item['name']=names[i]
            item['museum']=museum
            item['address']=museum
            page_url='http://www.zgnybwg.com.cn/'+page_urls[i]
            yield scrapy.Request(page_url,callback=self.parse_page,meta=item)

    def parse_page(self,response):
        item=response.meta
        time=response.xpath('//span[@class="time"]//text()').extract_first()
        item['time']=time.replace(' ','').replace('\n','')
        content=response.xpath("//div[@class='content']//text()").extract()
        content = ''.join(content).replace(' ', '').replace('\n', '').replace('\r', '').replace('\xa0', '').replace('\u3000e', '').replace('\t','').replace('\u3000','')
        item['introduce']=content
        yield item