import scrapy
from ..items import ShowinfoItem

class AirSpaceSpider(scrapy.Spider):

     name="AirSpider"
     start_urls=['http://airandspacemuseum.buaa.edu.cn/lszl/index.jhtml']

     def parse(self,response):
         museum="中国航空博物馆"
         content=response.xpath("//ul[@id='imgAuto']/li/div[@class='c_txt']")
         l=len(content)
         names=content.xpath("//h4/text()").extract()
         times=content.xpath("//p[2]/text()").extract()
         addresss=content.xpath("//p[3]/text()").extract()
         hrefs=content.xpath("//p[4]/a/@href").extract()
         for i in range(l):
             item=ShowinfoItem()
             item['museum']=museum
             item['name']=names[i]
             item['time']=times[i]
             item['address']=addresss[i]
             h=hrefs[i]
             yield scrapy.Request('http://airandspacemuseum.buaa.edu.cn'+h, callback=self.parse_content,meta=item)
         if response.xpath('//div[@class="page_box"]/a[4]/@href').extract_first():
            next_page='http://airandspacemuseum.buaa.edu.cn/lszl/'+response.xpath('//div[@class="page_box"]/a[4]/@href').extract_first()
            yield scrapy.Request(next_page,callback=self.parse)

     def parse_content(self,reponse):
          item=reponse.meta
          item['introduce']=''.join(reponse.xpath('//div[@class="content_box"]//text()').extract()).replace('\n','\t').replace('\t','').replace('\r','')
          yield item


