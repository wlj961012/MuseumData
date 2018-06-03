import scrapy
from ..items import ShowinfoItem

class ShangHaiSpider(scrapy.Spider):

    name="shanghaiSpider"
    start_urls=['http://www.shanghaimuseum.net/museum/frontend/display/exhibition-info-out-line-detail?exhibitionCode=E00004057']

    def parse(self, response):
        item=ShowinfoItem()

        museum="上海博物馆"

        name=response.xpath("//div/div[2]/div/div[2]/div/p[1]//text()").extract()
        '''
        time=response.xpath("//div/div[2]/div[4]/div/div/p[6]//text()").extract()[1]
        address=response.xpath("//div/div[2]/div[4]/div/div/p[7]//text()").extract()[1]
        introduce=response.xpath("//div/div[2]/div[4]/div/div/p[8]//text()").extract()[0]
        '''
        item['name'] = "心灵的风景"
        item['museum'] = museum
        item['time']="2018-04-27 ~ 2018-08-05 "
        item['address']="上海博物馆第二展厅"
        item['introduce']="风景于我们有着永恒的魅力。中国人素来深谙风景之趣，否则山水也无以成为中国画中的蔚然大宗，成为文士骚客可行、可望、可居、可游的精神归所，寄托着他们与隐逸、出世等等有关的梦想。推己及人，世界各地的所谓“风景艺术”同样不仅仅是对自然的再现；正如贡布里希所说：“天真纯洁的眼睛只是一个神话”，作为外部的风景终须由人摄取才能够以艺术的形式被呈现；那些选择、置换、安排和构造风景的手与眼，无法回避地带有文化预制的精神模板，反映着不同民族的文化心理与美学观念。"
        yield item
