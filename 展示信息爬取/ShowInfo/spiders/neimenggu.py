import scrapy
from ..items import ShowinfoItem

class NeiMengSpider(scrapy.Spider):

    name="NeiMengSpider"
    start_urls=['http://www.nmgbwy.com/zldt/1356.jhtml']

    def parse(self, response):

        museum="内蒙古博物院"

        name=response.xpath("//div/div[2]/div[4]/div/div/div/font//text()").extract()[0]
        item=ShowinfoItem()

        time=response.xpath("//div/div[2]/div[4]/div/div/p[6]//text()").extract()[1]
        address=response.xpath("//div/div[2]/div[4]/div/div/p[7]//text()").extract()[1]
        introduce=response.xpath("//div/div[2]/div[4]/div/div/p[8]//text()").extract()[0]

        item['name'] = name
        item['museum'] = museum
        item['time']=time
        item['address']=address
        item['introduce']=introduce
        yield item
