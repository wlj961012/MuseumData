import scrapy
from scrapy import Spider, Request
import requests
import lxml.html
from ..items import ShowinfoItem

class MintaiyuanSpider(scrapy.Spider):
    name = 'mintaiyuanmuseum'
    start_urls = ['http://www.mtybwg.org.cn/zhanlan2/104-1.aspx']
    museum="中国闽台缘博物院"

    def parse(self, response):
        res=response.xpath('//ul[@class="iflist"]/li')
        # print(len(res))
        for each in res:
            name=each.xpath('a/text()').extract()
            name="".join(name)

            url=each.xpath('a/@href').extract()
            url="".join(url)
            url="http://www.mtybwg.org.cn"+url
            html = requests.get(url).content
            selector = lxml.html.document_fromstring(html)
            introduce=selector.xpath('//ul[@class="detailcon"]/p//text()')
            introduce="".join(introduce)
            # print(introduce)

            time="临时展览"

            address="中国闽台缘博物院"

            item = ShowinfoItem()
            item['museum'] = self.museum
            item['name'] = name
            item['time'] = time
            item['address'] = address
            item['introduce'] = introduce

            yield item