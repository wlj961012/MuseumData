import scrapy
from ..items import ShowinfoItem

class ZhouenlaiSpider(scrapy.Spider):

    name="ZhouenlaiSpider"
    start_urls=['http://www.mzhoudeng.com/exhibits.aspx?cateid=87']

    def parse(self, response):

         museum='周恩来邓颖超纪念馆'
         names=response.xpath('//div[@class="exhibits"]/ul/li/a/div/div[1]//text()').extract()
         adds=response.xpath('//div[@class="exhibits"]/ul/li/a/div/div[2]//text()').extract()
         page_urls=response.xpath('//div[@class="exhibits"]/ul/li/a/@href').extract()
         l=len(names)

         for i in range(l):
             item=ShowinfoItem()
             item['museum']=museum
             item['name']=names[i]
             item['address']=adds[i+1]
             page_url='http://www.mzhoudeng.com/'+page_urls[i]

             yield scrapy.Request(page_url,callback=self.parse_page,meta=item)

    def parse_page(self,response):

         item=response.meta
         time=response.xpath('//div[@class="newsin_Tit02"]//text()').extract_first()
         item['time']=time
         introduce=response.xpath('//p//text()').extract()
         item['introduce'] = ''.join(introduce).replace('\n', '').replace('\r', '').replace(' ', '').replace('\xa0', '').replace("中文|ENGLISH|日本語",'')
         item['introduce']=item['introduce'].replace('版权所有周恩来邓颖超纪念馆津ICP备15008662号地址：天津市南开区水上公园西路9号邮编：300074电话：022-235922572310660823591821电子邮件：zhoudeng1@mzhoudeng.com周恩来邓颖超纪念馆微博：http://weibo.com/p/1001065700080604周恩来邓颖超纪念馆官方公众号:技术支持：35互联','')

         yield item


