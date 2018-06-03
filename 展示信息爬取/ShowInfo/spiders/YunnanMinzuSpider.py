import scrapy
from ..items import ShowinfoItem

class YunnanMinzuSpider(scrapy.Spider):

    name="YNMZSpider"
    start_urls=['http://www.ynnmuseum.com/products_detail/productId=95.html']

    def parse(self, response):
        item=ShowinfoItem()

        museum="云南民族博物馆"
        name=response.xpath("//div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div/form[1]/div[1]/div[2]/ul[1]/li[1]//text()").extract_first()
        introduce=response.xpath("//div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div/form[1]/div[2]/div/div/p//text()").extract()

        item['name'] = name
        item['museum'] = museum
        item['address'] = "云南省昆明市西山区滇池路1503号"
        item['time']="2011年12月25日"
        item['introduce']=''.join(introduce)

        yield item