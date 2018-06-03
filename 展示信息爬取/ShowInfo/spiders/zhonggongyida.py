import scrapy
from ..items import ShowinfoItem

class ZhongGongYiDaSpider(scrapy.Spider):

    name="zhonggongyidaSpider"
    start_urls=['http://www.luxunmuseum.cn/news/page/id/160.html']

    def parse(self, response):
        item=ShowinfoItem()

        museum="中共一大会址纪念馆"
        '''
        name=response.xpath("//div/div[1]/h2//text()").extract()[0]

        time=response.xpath("//div/div[1]/p//text()").extract()[0]
        #address=response.xpath("//div/div[2]/div[4]/div/div/p[7]//text()").extract()[1]
        introduce=response.xpath("//div/div[1]/div[2]/div/div/p[6]/span//text()").extract()[0]
        '''
        item['name'] ="《周恩来在上海》文物史料展"
        item['museum'] = museum
        item['time']="2018年3月5日至2018年4月25日"
        item['address']="中共一大会址纪念馆专题展厅"
        item['introduce']="此次展览通过大量的珍贵文物史料展现了周恩来一生与上海特殊而密切的关系。展览展出的54件珍贵文物中，包括周恩来亲笔题字的平型关大捷战利品——日军军用怀安地图；周恩来在扉页书写：“为真民主、真和平而奋斗到底”的书籍——《政协文献》等。展览还选取了123幅具有代表性的图片，以时间轴和专题版块的形式，回顾了周恩来领导上海工人第三次武装起义、指挥上海人民的抗日救亡运动、在周公馆开展广泛的爱国民主统一战线、指示上海地下党坚持斗争开辟第二条战线，到建国后对上海的经济、国防、科技、文化、体育等方面的指导与关心。为了配合此次展览主题，中共一大会址纪念馆还邀请了周恩来亲属代表周尔均将军、全国周恩来思想及生平研究会荣誉会长廖心文女士参加本次展览开幕式及纪念周恩来诞辰120周年情景音乐会。"
        yield item
