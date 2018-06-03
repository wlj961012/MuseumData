import scrapy
from scrapy import Spider, Request
import requests
import lxml.html
from ..items import ShowinfoItem

class JiangximuseumSpider(scrapy.Spider):
    name = 'ruijingmuseum'
    start_urls = ['http://www.rjjng.com.cn/display/']
    museum="瑞金中央革命根据地纪念馆"

    def parse(self, response):
        res=response.xpath('//ul[@id="view"]/li')
        for each in res:
            url=each.xpath('a/@href').extract()
            url="".join(url)
            name = each.xpath('a/@title').extract()
            name="".join(name)

            html = requests.get(url).content
            selector = lxml.html.document_fromstring(html)
            # introduce=selector.xpath('//div[@id="content_10"]/p//text()')
            #introduce=''.join(introduce)

            introduce=name

            time="常设展览"

            address="瑞金中央革命根据地纪念馆"

            item = ShowinfoItem()
            item['museum'] = self.museum
            item['name'] = name
            item['time'] = time
            item['address'] = address
            item['introduce'] = introduce

            yield item




