import scrapy
from ..items import ShowinfoItem

class ChongqingZiranSpider(scrapy.Spider):

    name="CQZRSpider"
    start_urls=['http://www.cmnh.org.cn/content/?166.html']

    def parse(self, response):
        item=ShowinfoItem()

        museum="重庆自然博物馆"
        name=response.xpath("//div/div[3]/div/h1//text()").extract()
        introduce=response.xpath("//div/div[3]/div/div[2]//text()").extract()

        item['name'] = name
        item['museum'] = museum
        item['address'] = "重庆市北碚区金华路398号"
        item['time']="周二至周日9:00-17:00（16:00停止入馆），周一闭馆（法定节假日除外）"
        item['introduce']=introduce

        yield item