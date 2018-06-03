import scrapy
from ..items import ShowinfoItem

class KangriSpider(scrapy.Spider):

    name="kangriSpider"
    start_urls=["http://www.1937china.com/clzl/ztzl/index.shtml"]

    def parse(self,response):

        item=ShowinfoItem()
        museum="中国人民抗日战争纪念馆"
        
        item['museum']=museum
        item['name']=""
        item['time']=""
        item["introduce"]=""
        item["address"]=""