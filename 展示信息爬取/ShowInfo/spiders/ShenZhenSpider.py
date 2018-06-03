import scrapy
from ..items import ShowinfoItem

class ShenZhenSpider(scrapy.Spider):

    name="ShenZhenSpider"
    start_urls=["https://www.shenzhenmuseum.com/exhibition/detail?resType=CmsExhibition&resId=e8c503a3f0714ec9a1b963b320ee1950"]

    def parse(self, response):

        museum="深圳博物馆"
        name=response.xpath("//div/div[1]/h2/span//text()").extract_first()
        time=response.xpath("//div/div[1]/div/div[1]/p//text()").extract_first()
        address=response.xpath("//div/div[1]/div/div[2]/p//text()").extract_first()
        introduce=response.xpath("//div/div[1]/div/div[3]/div/div[1]//text()").extract()

        item=ShowinfoItem()
        item['name']=name
        item['time']=time
        item['address']=address
        item['museum']=museum
        item['introduce']=''.join(introduce)


        yield item