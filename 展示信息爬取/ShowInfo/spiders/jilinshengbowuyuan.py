import scrapy
from ..items import ShowinfoItem

class JiLinSpider(scrapy.Spider):

    name="jilinSpider"
    start_urls=['http://www.jlmuseum.org/display/show/1599.html']

    def parse(self, response):

        museum="吉林省博物院"

        name=response.xpath("//div/div[2]/div[2]/h1//text()").extract()[0]
        item=ShowinfoItem()


        introduce=response.xpath("//div/div[2]/div[2]/div/p[2]//text()").extract()
        introduce=''.join(introduce).replace(' ','').replace('\r\n\t','').replace('\xa0','').replace('\r\n','')

        item['name'] = name
        item['museum'] = museum
        item['time']=""
        item['address']=""
        item['introduce']=introduce
        yield item
