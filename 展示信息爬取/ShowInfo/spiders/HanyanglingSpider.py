import scrapy
from ..items import ShowinfoItem

class YunnanMinzuSpider(scrapy.Spider):

    name="HYLSpider"
    start_urls=['http://www.hylae.com/list.asp?id=3729']

    def parse(self, response):
        item=ShowinfoItem()

        museum="汉阳陵博物馆"
        '''
        name=response.xpath("//div/div/table[2]/tbody/tr/td/table[2]/tbody/tr[1]/td//text()").extract()
        introduce=response.xpath("//div/div/table[2]/tbody/tr/td/table[2]/tbody/tr[2]/td/p[9]//text()").extract()
        '''

        item['name'] = "汉阳陵文物参加卡塔尔“华夏瑰宝展”"
        item['museum'] = museum
        item['address'] = "西安咸阳国际机场专线公路东段"
        item['time']="此次展览从2016年9月开始，截止到2017年1月结束。"
        item['introduce']="2016年9月6日，“华夏瑰宝展”在卡塔尔伊斯兰艺术博物馆开幕。中国驻卡塔尔大使李琛、卡塔尔博物馆管理局代理首席执行官曼苏尔及卡各界人士、各国驻卡使节等出席开幕式。本次“华夏瑰宝展”由中国国家文物局和卡塔尔博物馆管理局共同主办，中国文物交流中心和卡伊斯兰艺术博物馆合作承办，是2016中卡文化年的重头戏，也是中卡两国建交28年来中国在卡举办的规模最大、展品价值最高的一次展览，精选了来自故宫博物院、西安博物院、秦始皇帝陵博物院、汉阳陵博物院、半坡博物馆五家单位的陶器、青铜器、玉器、瓷器、金银器等85组116件文物展出，其中包括5件享誉世界的秦兵马俑。展览按照华夏文明的发展脉络，涵盖了从史前文化到明清时期的漫长历史岁月，以生动形象的方式向卡塔尔人民展现了华夏文明的博大精深和薪火传承。"

        yield item