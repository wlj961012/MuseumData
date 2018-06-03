import scrapy
import requests
import lxml.html
from ..items import ShowinfoItem

class FujianSpider(scrapy.Spider):
    name = 'fujianmuseum'
    start_urls = ['http://museum.fjsen.com/node_167181.htm']
    museum="福建博物院"

    def parse(self, response):
        res=response.xpath('//div[@class="cont-left"]/ul/li')
        for each in res:
            name=each.xpath('a/text()').extract()
            name=''.join(name)

            url=each.xpath('a/@href').extract()
            url=''.join(url)
            url="http://museum.fjsen.com/"+url
            html = requests.get(url).content
            selector = lxml.html.document_fromstring(html)
            introduce=selector.xpath('///td[@id="new_message_id"]/p//text()')
            introduce=''.join(introduce)
            address="福建博物院"
            time="常设展览"

            item = ShowinfoItem()
            item['museum'] = self.museum
            item['name'] = name
            item['time'] = time
            item['address'] = address
            item['introduce'] = introduce

            yield item

