import scrapy
from ..items import ShowinfoItem

class TianwenSpider(scrapy.Spider):

    name="TianWenSpider"
    start_urls=["http://www.bjp.org.cn/art/2015/2/11/art_156_4238.html"]

    def parse(self,response):

        museum="北京天文馆"
        item=ShowinfoItem()
        introduce=response.xpath("//p//text()").extract()
        introduce=''.join(introduce).replace('\xa0','').replace(' ','')
        item['introduce']=introduce
        item['museum']=museum
        item['address']=museum
        name=response.xpath('//table[@width="100%"]/tr/td[2]//text()').extract()[-1]
        item['name']=name
        time='2015-02-11'
        item['time']=time
        yield item