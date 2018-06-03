import scrapy
from ..items import ShowinfoItem

class SanXing(scrapy.Spider):

    name="SanXing"
    start_urls=['http://www.sxd.cn/showinfo.asp?id=12&bigclass=23']

    def parse(self, response):

        museum='三星堆博物馆'
        item=ShowinfoItem()
        item['museum']=museum
        name=response.xpath('//div/div[2]/div[2]/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[1]/td//text()').extract_first()
        if name:
            item['name']=name
        else:
            item['name']=''
        time=response.xpath('//div/div[2]/div[2]/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/p[7]/font//text()').extract_first()
        if time:
            item['time']=time
        else:
            item['time']=''
        address=response.xpath('//div/div[2]/div[2]/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/p[1]/font/text()[2]//text()').extract_first()
        if address:
            item['address']=address
        else:
            item['address']=''
        introduce=response.xpath('//div/div[2]/div[2]/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/p//text()').extract()
        introduce=''.join(introduce)
        if introduce:
            item['introduce']=introduce
        else:
            item['introduce']=''

        yield item