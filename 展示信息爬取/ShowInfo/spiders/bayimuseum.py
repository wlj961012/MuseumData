import scrapy
import requests
import lxml.html
from ..items import ShowinfoItem

class BayiSpider(scrapy.Spider):
    name = 'bayimuseum'
    start_urls = ['http://www.81-china.com/zhanlan/57.html']
    museum="南昌八一起义纪念馆"

    def parse(self, response):
        res=response.xpath('//div[@class="list_content"]/ul[@class="list_ul"]/li')
        for each in res:
            name=each.xpath('div[@class="right_listcon"]/h3/a/text()').extract()
            name="".join(name)

            url=each.xpath('div[@class="right_listcon"]/h3/a/@href').extract()
            url="".join(url)
            url="http://www.81-china.com"+url
            html = requests.get(url).content
            selector = lxml.html.document_fromstring(html)
            introduce=selector.xpath('//div[@class="detial_txt"]/p//text()')
            introduce="".join(introduce)

            address="南昌八一起义纪念馆"

            time="常设展览"

            item = ShowinfoItem()
            item['museum'] = self.museum
            item['name'] = name
            item['time'] = time
            item['address'] = address
            item['introduce'] = introduce

            yield item
