import scrapy
from ..items import ShowinfoItem

class XianBeilinSpider(scrapy.Spider):

    name="BeilinSpider"
    start_urls=['http://www.beilin-museum.com/contents/17/3677.html']

    def parse(self, response):
        item=ShowinfoItem()

        museum="西安碑林博物馆"
        name=response.xpath("//div/div[1]//text()").extract_first()
        introduce=response.xpath("//div/div[3]//text()").extract()

        item['name'] = name
        item['museum'] = museum
        item['address'] = "西安碑林博物馆东临展室"
        item['time']="2013年"
        item['introduce']=''.join(introduce)

        yield item