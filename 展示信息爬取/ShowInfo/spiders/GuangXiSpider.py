import scrapy
from ..items import ShowinfoItem


class GuangXiSpider(scrapy.Spider):
    name = "GuangXiSpider"
    start_urls = ['http://www.gxmuseum.cn/a/exhibition/13/2018/7663.html']

    def parse(self, response):
        museum = "广西壮族自治区博物馆"

        name = response.xpath("//div/div[2]/div[2]/div[2]/div[1]/h2//text()").extract_first()
        time = response.xpath("//div/div[2]/div[2]/div[2]/div[2]/text()//text()").extract_first()
        introduce = response.xpath("//*[@id='contentText']/p[1]//text()").extract()

        item = ShowinfoItem()
        if name:
            item['name'] = name
        else:
            item['name']=''
        if time:
            item['time']=time
        else:
            item['time']=''
        item['address'] = museum
        item['museum'] = museum
        if introduce:
            item['introduce'] = ''.join(introduce)
        else:
            item['introduce']=''

        yield item