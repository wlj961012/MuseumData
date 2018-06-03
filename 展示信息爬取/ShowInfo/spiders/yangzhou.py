import scrapy
from ..items import ShowinfoItem

class YangZhouSpider(scrapy.Spider):

    name="yangzhouSpider"
    start_urls=['http://www.yzmuseum.com/website/exhibition/detail.php?id=1165']

    def parse(self, response):
        item=ShowinfoItem()

        museum="扬州博物馆"

        name=response.xpath("//div/div[2]/div[2]/div[3]/div[3]/p[1]//text()").extract()[0]

        time=response.xpath("//div/div[2]/div[2]/div[3]/div[3]/p[2]//text()").extract()[0]
        address=response.xpath("//div/div[2]/div[2]/div[3]/div[3]/p[3]//text()").extract()[0]
        introduce=response.xpath("//div/div[2]/div[2]/div[3]/div[3]/p[3]//text()").extract()[0]

        item['name'] =name
        item['museum'] = museum
        item['time']=time
        item['address']=address
        item['introduce']=introduce
        yield item
