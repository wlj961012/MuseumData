import scrapy
from ..items import ShowinfoItem

class NanJingSpider(scrapy.Spider):

    name="nanjingSpider"
    start_urls=['http://www.luxunmuseum.cn/news/page/id/160.html']

    def parse(self, response):
        item=ShowinfoItem()

        museum="南京博物院"

        #name=response.xpath("//form/div[4]/div[2]/div[1]/div/div[2]/div[3]/div[2]/ul/li[1]//text()").extract()

        #time=response.xpath("//div/div[1]/p//text()").extract()[0]
        #address=response.xpath("//div/div[2]/div[4]/div/div/p[7]//text()").extract()[1]
        #introduce=response.xpath("//div/div[1]/div[2]/div/div/p[6]/span//text()").extract()[0]

        item['name'] ="回家过年"
        item['museum'] = museum
        item['time']="2018.2.2—4.10"
        item['address']="特展馆2楼8号展厅"
        item['introduce']="戊戌来临，南京博物院策划了以“回家过年”为主题的展览。展览以“家”“年”和“年代感”为关键词，以新中国成立以来家庭生活状态变迁为轴，通过场景、实物、影像、装置等，将过去的年味“搬到”今天，让今天的年味概念化呈现。该展不同于南博以往推出的春节系列展，这次展览可触摸、可把玩、可落座，让观众身临其境、宾至如归，希望每一个家庭都能在展览中找到自己家的影子，希望每一位家庭成员都能在展览中看到曾经过年的样子。"
        yield item
