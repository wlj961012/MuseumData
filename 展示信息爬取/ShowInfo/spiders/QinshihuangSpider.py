import scrapy
from ..items import ShowinfoItem

class QinshihuangSpider(scrapy.Spider):

    name="QinSpider"
    start_urls=['http://www.bmy.com.cn/2015new/contents/489/23679.html']

    def parse(self, response):
        item=ShowinfoItem()

        museum="秦始皇帝陵博物院（秦始皇兵马俑博物馆）"
        name=response.xpath("//div/div[3]/div[2]/div[3]/p[3]/span[2]//text()").extract_first()
        time=response.xpath("//div/div[3]/div[2]/div[3]/p[4]//text()").extract_first()
        introduce=response.xpath("//div/div[3]/div[2]/div[3]/p[6]//text()").extract()

        item['name'] = name
        item['museum'] = museum
        item['address'] = "陕西省西安市临潼区"
        item['time']=''.join(time)
        item['introduce']=''.join(introduce)

        yield item