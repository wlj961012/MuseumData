import scrapy
from ..items import ShowinfoItem

class GugongSpider(scrapy.Spider):

    name='GugongSpider'
    start_urls=['http://www.dpm.org.cn/subject_althani/preface.html']

    def parse(self, response):

        museum='故宫博物院'
        name='铭心撷珍——卡塔尔阿勒萨尼收藏展'
        time='2018/04/17 - 2018/06/18'
        address='午门及西雁翅楼展厅'
        item=ShowinfoItem()
        item['name']=name
        item['time']=time
        item['address']=address
        item['museum']=museum
        introduce=response.xpath('//p//text()').extract()
        item['introduce']=''.join(introduce)
        print(item)
        yield item
