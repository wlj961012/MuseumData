import scrapy
from scrapy import Spider, Request
import requests
import lxml.html
from ..items import ShowinfoItem

class YantaimuseumSpider(scrapy.Spider):
    name = 'yantaimuseum'
    start_urls = ['http://www.ytmuseum.com/zhanting/Psort_yugao/List.html']
    museum="烟台博物馆"

    def parse(self, response):
        res=response.xpath('//div[@id="MainLeft"]/div/div/ul/li')

        for each in res:
            url=each.xpath('div[2]/a/@href').extract()
            url=''.join(url)
            url="http://www.ytmuseum.com"+url
            name=each.xpath('div[2]/a/text()').extract_first()

            html = requests.get(url).content
            selector = lxml.html.document_fromstring(html)
            introduce=selector.xpath('div[@id="MainLeft"]/div/tabel/tr[3]/td/p//text()')
            # introduce=''.join(introduce)
            introduce="馆庆三大主题展览之二，以“四时”为线，与观众一起跟随文物的脚步，走过岁月，走向明天。本次展览展出的展品，源自烟台市博物馆六十年来积累的馆藏资源，其中有大家耳熟能详的包括镇馆之宝在内的国家三级以上珍贵文物、文物普查中新发现的馆藏遗珠及由文物店移交过来的珍贵藏品。"

            time="常设展览"

            address="烟台博物馆"

            item = ShowinfoItem()
            item['museum'] = self.museum
            item['name'] = name
            item['time'] = time
            item['address'] = address
            item['introduce'] = introduce

            yield item






