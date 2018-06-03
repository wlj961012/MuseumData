import scrapy
from ..items import ShowinfoItem

class JiLinNatureSpider(scrapy.Spider):

    name="jilinnatureSpider"
    start_urls=['http://museum.nenu.edu.cn/info/1019/1762.htm']

    def parse(self, response):

        museum="吉林省自然博物馆"

        name=response.xpath("//div/form/div/div[1]/p[2]/strong/span//text()").extract()[0]
        item=ShowinfoItem()


        introduce=response.xpath("//div/form/div/div[1]/p[3]/span//text()").extract()[0].replace('\xa0','')

        item['name'] = name
        item['museum'] = museum
        item['time']="2017年11月27日至2018年3月26日"
        item['address']="长白山自然博物馆"
        item['introduce']=introduce
        yield item
