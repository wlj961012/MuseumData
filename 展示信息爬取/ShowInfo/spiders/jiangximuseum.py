import scrapy
import requests
import lxml.html
from ..items import ShowinfoItem

class JiangximuseumSpider(scrapy.Spider):
    
    name = 'jiangximuseum'
    start_urls = ['http://www.jxmuseum.cn/Exhibition/TempDisplayList/lzhg']
    museum="江西省博物馆"

    def parse(self, response):
        res=response.xpath('//div[@id="divList"]/ul[@class="exbitlist"]/li')
        for each in res:
            name=each.xpath('div/a/h3[@class="ellipsis"]/text()').extract()
            name=''.join(name)

            time=each.xpath('div/p[1]/text()').extract()
            time=''.join(time)

            address=each.xpath('div/p[2]/text()').extract()
            address=''.join(address)

            url=each.xpath('div/a/@href').extract()
            url="http://www.jxmuseum.cn"+url[0]


            html = requests.get(url).content
            selector = lxml.html.document_fromstring(html)
            introduce=selector.xpath('/html/body/div[3]/div/div/div[2]/div[2]/p//text()')
            introduce = ''.join(introduce)

            item = ShowinfoItem()
            item['museum'] = self.museum
            item['name'] = name
            item['time'] = time
            item['address'] = address
            item['introduce'] = introduce

            yield item
