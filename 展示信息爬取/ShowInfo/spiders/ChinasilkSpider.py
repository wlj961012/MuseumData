import scrapy
from ..items import ShowinfoItem

class ChinasilkSpider(scrapy.Spider):

    name='SilkSpider'
    start_urls=['http://www.chinasilkmuseum.com/zz/info_17.aspx?itemid=26693']

    def parse(self,response):

        museum='中国丝绸博物馆'
        name=response.xpath('//div/div/div[3]/div/div[1]/div[1]//text()').extract_first()
        time=response.xpath('//div/div/div[3]/div/div[2]/p[10]//text()').extract_first()
        address=response.xpath('//div/div/div[3]/div/div[2]/p[9]//text()').extract_first()
        introduce=response.xpath('//div[@class="detail_text"]').xpath('string(.)').extract_first()
        item=ShowinfoItem()
        item['museum']=museum
        item['name']=name
        item['time']=time
        item['address']=address
        item['introduce']=''.join(introduce).replace('Cultural Relics from Changganli: Silk of the Song Dynasty Unearthed from the Grand Baoen Temple Nanjing主办：中国丝绸博物馆      南京市博物总馆      南京市考古研究所展览地点：中国丝绸博物馆修复展示馆展览时间：2018.4.4-2018.6.25OrganizersChina National Silk Museum, Nanjing Museum, Nanjing Institute of ArchaeologyDurationApril 4 – June 25, 2018Venue Textile Conservation Gallery','')

        yield item