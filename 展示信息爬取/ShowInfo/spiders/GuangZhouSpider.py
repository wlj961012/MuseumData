import scrapy
from ..items import ShowinfoItem

class GuangZhouSpider(scrapy.Spider):

    name="GuangZhouSpider"
    start_urls=["http://www.guangzhoumuseum.cn/main.asp"]

    def parse(self, response):

        museum="广州博物馆"
        name=response.xpath("//table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/table/tbody/tr[3]/td[2]//text()").extract_first()
        time=response.xpath("//table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/table/tbody/tr[4]/td[2]/div/p[3]/font/text()[3]//text()").extract_first()
        address=response.xpath("//table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/table/tbody/tr[4]/td[2]/div/p[3]/font/text()[2]//text()").extract_first()
        introduce = response.xpath("//table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/table/tbody/tr[4]/td[2]/div/font/p//text()").extract()

        item=ShowinfoItem()
        if name:
            item['name']=name
        else:
            item['name']=""
        if time:
            item['time']=time
        else:
            item['address']=address
        if museum:
            item['museum']=museum
        else:
            item['museum']=''
        if introduce:
            item['introduce'] = ''.join(introduce)
        else:
            item['introduce']=''

        yield item