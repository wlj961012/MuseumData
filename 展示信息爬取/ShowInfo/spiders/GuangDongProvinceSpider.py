import scrapy
from ..items import ShowinfoItem

class GuangDongProvinceSpider(scrapy.Spider):

    name="GuangDongProvinceSpider"
    start_urls=["http://www.gdmuseum.com/gdmuseum/_300730/zlyg/495299/index.html"]

    def parse(self, response):

        museum="广东省博物馆"
        name=response.xpath("//*[@id='jianjie_content']/div[1]/div[1]//text()").extract_first()
        time=response.xpath("//*[@id='jianjie_content']/div[1]/div[2]//text()").extract_first()
        address=response.xpath("//*[@id='jianjie_content']/div[1]/div[2]//text()").extract_first()
        introduce=response.xpath("//*[@id='menu_list2']/div[3]/p[7]//text()").extract()

        item=ShowinfoItem()
        item['name']=name
        item['time']=time
        item['address']=address
        item['museum']=museum
        item['introduce']=''.join(introduce)

        yield item