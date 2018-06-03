import scrapy
from ..items import ShowinfoItem

class wenzhaouSpider(scrapy.Spider):

    name='wzSpider'
    start_urls=['https://www.wzmuseum.cn/Art/Art_22/Art_22_1945.aspx']

    def parse(self, response):

        museum='温州博物馆'
        name=response.xpath('//div[@class="tit"]/b//text()').extract_first()
        time=response.xpath('//div/div[1]/div/div/div[3]/div[2]/div[2]/p[7]/span//text()').extract_first()
        address=response.xpath('//div/div[1]/div/div/div[3]/div[2]/div[2]/p[4]/span/span//text()').extract_first()
        introduce=response.xpath('//div[@class="con"]//text()').extract()
        #print(museum,name,time,address,introduce)
        item=ShowinfoItem()
        item['name']=name
        item['museum']=museum
        item['time']=time
        item['address']=address
        item['introduce']=''.join(introduce).replace(time,'').replace(address,'').replace('展览时间：','').replace("展览地点：","")

        yield item

