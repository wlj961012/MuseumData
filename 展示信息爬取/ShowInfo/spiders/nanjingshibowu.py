import scrapy
from ..items import ShowinfoItem

class NanJingshibowuSpider(scrapy.Spider):

    name="NanJingshiSpider"
    start_urls=['http://www.njmuseumadmin.com/Exhibition/show/id/132']

    def parse(self, response):
        item=ShowinfoItem()

        museum="南京市博物总馆"

        name=response.xpath("//div/div[3]/div[2]/div/div[2]/span//text()").extract()[0]

        time=response.xpath("//div/div[3]/div[2]/div/div[2]/dl/dt[1]/b//text()").extract()[0]
        address=response.xpath("//div/div[3]/div[2]/div/div[2]/dl/dt[2]/b//text()").extract()[0]
        #introduce=response.xpath("//div/div[3]/div/div[2]/p[40]//text()").extract()[0]

        item['name'] =name
        item['museum'] = museum
        item['time']=time
        item['address']=address
        item['introduce']="展览由“狗年话狗”、“犬文化大观”、“狗年习俗”三部分组成。南京市博物总馆除献展所藏狗类题材文物外，还结合展览主题展出犬贺新春内容的非遗工艺、红色喜庆的传统民俗物件以及时尚创意的现代文创，展览还为非遗文化传承者搭建起展现技艺的平台，呈现丰富趣味的互动活动，展现博物总馆近年在文化传承方面的开拓与创新。"
        yield item
