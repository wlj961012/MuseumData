import scrapy
from ..items import ShowinfoItem

class ShangHaiKejiSpider(scrapy.Spider):

    name="shanghaikejiSpider"
    start_urls=['http://www.luxunmuseum.cn/news/page/id/160.html']

    def parse(self, response):
        item=ShowinfoItem()

        museum="上海科技馆"
        '''
        name=response.xpath("//div/div[1]/h2//text()").extract()[0]

        time=response.xpath("//div/div[1]/p//text()").extract()[0]
        #address=response.xpath("//div/div[2]/div[4]/div/div/p[7]//text()").extract()[1]
        introduce=response.xpath("//div/div[1]/div[2]/div/div/p[6]/span//text()").extract()[0]
        '''
        item['name'] ="拉斯科洞穴壁画复原展"
        item['museum'] = museum
        item['time']="2017.11.1"
        item['address']="二楼特展厅"
        item['introduce']="展览以洞穴传奇的历史为主线，通过5组真实大小的复制洞壁、4个栩栩如生的克罗马农人雕像、17段生动影像等，结合互动游戏和珍贵图文，引领观众走进拉斯科世界，与2万年前的洞穴古人面对面，欣赏人类最早的艺术壮举，了解科学家、史前人类学家和艺术家是怎样研究、保护并复制这些珍贵的壁画的。展览通过艺术与技术的联姻，带领观众领略不朽的史前艺术，身临其境地感受克罗马农人的真实生活。"
        yield item
