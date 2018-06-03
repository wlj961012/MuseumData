import scrapy
from ..items import ShowinfoItem

class ShangHaiLuXunSpider(scrapy.Spider):

    name="shanghailuxunSpider"
    start_urls=['http://www.luxunmuseum.cn/news/page/id/160.html']

    def parse(self, response):
        item=ShowinfoItem()

        museum="上海鲁迅博物馆"

        name=response.xpath("//div/div[1]/h2//text()").extract()[0]

        time=response.xpath("//div/div[1]/p//text()").extract()[0]
        #address=response.xpath("//div/div[2]/div[4]/div/div/p[7]//text()").extract()[1]
        introduce=response.xpath("//div/div[1]/div[2]/div/div/p[6]/span//text()").extract()[0]

        item['name'] =name
        item['museum'] = museum
        item['time']=time
        item['address']="底楼活动厅"
        item['introduce']=introduce
        yield item
