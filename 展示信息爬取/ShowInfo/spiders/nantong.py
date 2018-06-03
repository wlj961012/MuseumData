import scrapy
from ..items import ShowinfoItem

class NanTongSpider(scrapy.Spider):

    name="nantongSpider"
    start_urls=['http://www.ntmuseum.com/m/news/exhnews/2442.html']

    def parse(self, response):
        item=ShowinfoItem()

        museum="南通博物苑"

        name=response.xpath("//div/article/h1//text()").extract()[0]

        time=response.xpath("//div/article/div/div[1]/span//text()").extract()[0]
        address=response.xpath("//div/article/div/div[2]/span//text()").extract()[0]
        #introduce=response.xpath("//div/div[1]/div[2]/div/div/p[6]/span//text()").extract()[0]

        item['name'] =name
        item['museum'] = museum
        item['time']=time
        item['address']=address
        item['introduce']=""
        yield item
