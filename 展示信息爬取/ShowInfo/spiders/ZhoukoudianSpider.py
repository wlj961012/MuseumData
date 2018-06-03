import scrapy
from ..items import ShowinfoItem

class ZhoukoudianSpider(scrapy.Spider):

     name="Zhoukoudian"
     start_urls=["http://www.zkd.cn/zlhg/index.jhtml"]

     def parse(self, response):


         museum="周口店猿人遗址博物馆"
         names=response.xpath("//div[@class='zlhg_list']/ul/li/a//text()").extract()
         page_urls=response.xpath("//div[@class='zlhg_list']/ul/li/a/@href").extract()
         times=response.xpath("//div[@class='zlhg_list']/ul/li/span//text()").extract()
         l=len(names)

         for i in range(l):
             item=ShowinfoItem()
             name=names[i]
             time=times[i]
             page_url=page_urls[i]
             item['name']=name
             item['time']=time
             item['museum']=museum
             yield scrapy.Request(page_url,callback=self.parse_page,meta=item)

     def parse_page(self,response):

         item=response.meta
         content=response.xpath("//div/div[1]/div[4]").xpath("string(.)").extract()

         if content:
             item['introduce']=''.join(content).replace(' ','').replace('\n','').replace('\r','').replace('\xa0','').replace('\u3000e','').replace('\t','').replace("分享到：腾讯新浪人人网邮件收藏夹复制网址更多varjiathis_config={data_track_clickback:true};","")
             item['address']="周口店猿人遗址博物馆"

             yield item
