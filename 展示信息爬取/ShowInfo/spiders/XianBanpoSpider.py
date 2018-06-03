import scrapy
from ..items import ShowinfoItem

class XianBanpoSpider(scrapy.Spider):

    name="BanpoSpider"
    start_urls=['http://www.bpmuseum.com/contents/120/1308.html']

    def parse(self, response):
        item=ShowinfoItem()

        museum="西安半坡博物馆"
        '''
        name=response.xpath("//table/tbody/tr[1]/td/table/tbody/tr/td[1]/table[2]/tbody/tr/td/div[1]//text()").extract()
        introduce=response.xpath("//table/tbody/tr[1]/td/table/tbody/tr/td[1]/table[2]/tbody/tr/td/div[3]//text()").extract()
        '''

        item['name'] = "西安半坡博物馆举办“纳西族东巴文化展”"
        item['museum'] = museum
        item['address'] = "西安半坡博物馆临展厅"
        item['time']="该展览将展出至2017年2月24日"
        item['introduce']="2016年11月24日，由西安半坡博物馆与丽江市博物院联合举办的《纳西族东巴文化展》在西安半坡博物馆临展厅展出。作为世界上收藏东巴文化文物类型最丰富的博物馆，丽江市博物院有着众多的东巴文化文物。此次展览展出纳西族东巴文化藏品191件，包括神路图、东巴经书、东巴舞谱、东巴应用文献、东巴纸牌画、木牌画、东巴文具、纳西象形文字雕版、五幅冠、东巴法器等种类，分为纳西族与东巴文化；东巴教及其仪式；纳西象形文及文献；东巴宗教艺术；东巴文化的研究与传承五大部分内容，将全面展示纳西族东巴文化的丰富内涵，让观众通过展览，走近丽江，了解丽江的历史文化、民族风情。"

        yield item