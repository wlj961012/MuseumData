import scrapy
from ..items import ShowinfoItem

class ShaanxiLishiSpider(scrapy.Spider):

    name="SXLSSpider"
    start_urls=['http://www.sxhm.com/index.php?ac=article&at=read&did=11798']

    def parse(self, response):
        item=ShowinfoItem()

        museum="陕西历史博物馆"
        name=response.xpath("//div/div[2]/div[2]/div[1]//text()").extract_first()
        time=response.xpath("//div/div[2]/div[2]/div[3]/p[11]//text()").extract_first()
        address=response.xpath("//div/div[2]/div[2]/div[3]/p[12]/span//text()").extract_first()
        introduce=response.xpath("//div/div[2]/div[2]/div[3]/p[7]//text()").extract()+response.xpath("//div/div[2]/div[2]/div[3]/p[8]//text()").extract()+response.xpath("//div/div[2]/div[2]/div[3]/p[9]//text()").extract()

        item['name'] = name
        item['museum'] = museum
        item['address'] = address
        item['time']=time
        item['introduce']=''.join(introduce)

        yield item