import scrapy
from ..items import ShowinfoItem

class LuoYangSpider(scrapy.Spider):

    name='LuoYangSpider'
    start_urls=['http://www.lymuseum.com/bencandy.php?fid=61&id=60']

    def parse(self,response):

        museum='洛阳博物馆'
        item=ShowinfoItem()
        item['museum']=museum
        name=''
        item['name']=name
        time=''
        item['time']=time
        address=''
        item['address']=address
        introduce=''
        item['introduce']=introduce
        yield item
