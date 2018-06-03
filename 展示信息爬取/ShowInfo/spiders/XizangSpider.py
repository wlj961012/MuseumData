import scrapy
from ..items import ShowinfoItem

class XizangSpider(scrapy.Spider):

    name="XizangSpider"
    start_urls=['http://www.tibetmuseum.cn/content/view_expo_new/bf6cq1UKRE6JPlMGSVpDT59rzt09hMXP']

    def parse(self, response):
        item=ShowinfoItem()

        museum="西藏博物馆"
        '''
        name=response.xpath("//div/div/div[2]/p[1]//text()").extract()
        time=response.xpath("//div/div/div[3]/div/p[1]/span//text()").extract()
        address=response.xpath("//div/div[3]/div/p[2]/span//text()").extract()
        introduce=response.xpath("//div/div[3]/div/p[6]/span//text()").extract()
        '''
        item['name'] = "祥云托起珠穆朗玛——藏传佛教艺术展"
        item['museum'] = museum
        item['address'] = "深圳、大连、宁夏、成都等地"
        item['time']= "2017年-2020年"
        item['introduce']="佛教自公元七世纪由中原和尼泊尔传入西藏后，巧妙融合传统苯教的元素，同时吸收印度、克什米尔和尼泊尔密教的精华，形成了具有鲜明民族特色和地域特征的藏传佛教。以唐卡、造像等为主要表现形式的藏传佛教艺术，表现了高原人民丰富的想象力和别具一格的审美情趣。本展览集布达拉宫、罗布林卡、西藏博物馆等西藏自治区内多家文物收藏机构的藏传佛教文物精品，包括蜚声海内外的唐卡、妙相庄严的造像、内容丰富的典籍、神态夸张的面具和工艺精良的法器，力图通过文物精品架起世人了解、认知、赏析藏传佛教文化艺术的桥梁。"

        yield item