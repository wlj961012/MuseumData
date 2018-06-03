import scrapy
from ..items import ShowinfoItem

class HeilogjiangSpider(scrapy.Spider):

    name="heilongjiangSpider"
    start_urls=['http://www.hljmuseum.com/system/201709/102964.html']

    def parse(self, response):
        item=ShowinfoItem()

        museum="黑龙江省博物馆"

        name=response.xpath("//div/div[3]/div/div[1]/div[2]/h2//text()").extract()[0]
        address=response.xpath("//div/div[3]/div/div/div[2]/div/p[4]/span//text()").extract()[0]
        introduce=response.xpath("//div/div[3]/div[1]/div[1]/div[2]/div[1]/p[13]/span//text()").extract()[0]

        item['name'] = name
        item['museum'] = museum
        item['time']="2017年9月28日——10月28日"
        item['address']=address
        item['introduce']=introduce
        yield item
