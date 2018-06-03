import scrapy
from scrapy import Spider, Request
import requests
import lxml.html
from ..items import ShowinfoItem

class QuanzhouSpider(scrapy.Spider):
    name = 'quanzhoumuseum'
    start_urls = ['http://www.qzhjg.com/gdzl/index.jhtml']
    museum="泉州海外交通博物馆"

    def parse(self, response):
        res=response.xpath('//div[@class="exhibitionList"]/ul/li')
        for each in res:
            name=each.xpath('div[@class="info"]/h3/text()').extract()
            name="".join(name)

            url=each.xpath('div[@class="info"]/a/@href').extract()
            url="".join(url)
            html = requests.get(url).content
            selector = lxml.html.document_fromstring(html)
            introduce=selector.xpath('//div[@class="detail_con"]/p//text()')
            introduce="".join(introduce)

            time="基本陈列"

            address="泉州海外交通博物馆"

            item = ShowinfoItem()
            item['museum'] = self.museum
            item['name'] = name
            item['time'] = time
            item['address'] = address
            item['introduce'] = introduce

            yield item