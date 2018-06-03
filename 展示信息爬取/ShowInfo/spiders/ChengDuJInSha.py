import scrapy
from ..items import ShowinfoItem

class ChengDuJinSha(scrapy.Spider):

    name="ChengDuJinSha"
    start_urls=['http://http://www.jinshasitemuseum.com/chenlie/201205/7.html']

    def parse(self,response):

            item=ShowinfoItem()

            museum="成都金沙遗址博物馆"

            item['name'] = ""
            item['museum'] = museum
            item['time']=""
            item['address']=""
            item['introduce']=""
            yield item
