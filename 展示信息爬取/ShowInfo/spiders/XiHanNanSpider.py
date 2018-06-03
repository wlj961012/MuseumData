import scrapy
from ..items import ShowinfoItem

class XiHanNanSpider(scrapy.Spider):

    name="XiHanNanSpider"
    start_urls=["http://www.gznywmuseum.org/info_114.aspx?itemid=1732"]

    def parse(self, response):

        museum="西汉南越王博物馆"
        name = response.xpath("//div/div[2]/div[2]/div[1]//text()").extract_first()
        time = response.xpath("//div[3]/div[2]/div[2]/div[3]/p[4]//text()").extract_first()
        introduce = response.xpath("//div/div[2]/div[2]/div[3]/p[3]/span[3]//text()").extract()

        item = ShowinfoItem()
        item['name'] = name
        item['time'] = time
        item['address'] = ""
        item['museum'] = museum
        item['introduce'] = introduce

        yield item