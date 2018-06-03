import scrapy
from ..items import ShowinfoItem

class YananSpider(scrapy.Spider):

    name="YananSpider"
    start_urls=['http://www.yagmjng.com/rsf/site/jinianguan/index.html']

    def parse(self, response):
        item=ShowinfoItem()

        museum="延安革命纪念馆"
        item['museum'] = museum
        item['name'] = ''
        item['time'] = ''
        item['address'] = ''
        item['introduce'] = ''

        yield item