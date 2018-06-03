import scrapy
from scrapy import Spider, Request
import requests
import lxml.html
from ..items import ShowinfoItem

class QingdaomuseumSpider(scrapy.Spider):
    name = 'qingdaomuseum'
    start_urls = ['http://www.qingdaomuseum.com/exhibition/category/16']
    museum="青岛博物馆"

    def parse(self, response):
        res=response.xpath('//div[@class="row zl_list"]/div[@class="col-xs-12 col-md-4"]')
        i=-1
        for each in res:
            i+=1
            name=each.xpath('//div[@class="zl_text"]/h4/text()').extract()
            name=name[i]

            url=each.xpath('div[@class="caption"]/a/@href').extract()
            url=''.join(url)
            html = requests.get(url).content
            selector = lxml.html.document_fromstring(html)
            introduce=selector.xpath('//div[@class="hd_nr"]/p/text()')
            introduce=''.join(introduce)

            time="常设展览"

            address="青岛市博物馆"

            item=ShowinfoItem()
            item['museum']=self.museum
            item['name']=name
            item['time']=time
            item['address']=address
            item['introduce']=introduce

            yield item







