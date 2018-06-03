import scrapy
from ..items import ShowinfoItem

class WeiManSpider(scrapy.Spider):

    name="weimanSpider"
    start_urls=['http://www.wmhg.com.cn/web/cn/portal/132773150355751544.htm?itmId=150654307378791566']

    def parse(self, response):
        item=ShowinfoItem()

        museum="伪满皇宫博物院"
        '''
        name=response.xpath("//p[@align='center']").extract()
        time=response.xpath("//div/div[2]/div[2]/div[2]/div[1]/div[2]/div/p[8]/span//text()").extract()


        address=response.xpath("//div/div[2]/div[2]/div[2]/div[1]/div[2]/div/p[9]/span//text()").extract()
        introduce=response.xpath("//div/div[2]/div[2]/div[2]/div[1]/div[2]/div/p[68]//text()").extract()
        '''
        item['name'] = "历史印迹  清宫帝后宝玺展"
        item['museum'] = museum
        item['time']="2017年9月20日-2018年4月8日"
        item['address']="伪满皇宫博物院怀远楼清宴堂"
        item['introduce']="“历史印迹——清宫帝后宝玺特展”由伪满皇宫博物院与故宫博物院联合推出，与旧影展同日开展。本次展出的玺印是从北京故宫博物院的2万多件玺印中精选80件，分国宝、皇帝宝玺、后妃玺册、宫殿宝玺、官印及合符、印样及印料等六个单元，集萃了清宫宝玺的菁华。"
        yield item
