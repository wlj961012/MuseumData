import scrapy
from ..items import ShowinfoItem

class LvSpider(scrapy.Spider):

    name="lvSpider"
    start_urls=['http://www.lvshunmuseum.org/Exhibition/ProductDetail.aspx?ID=276']

    def parse(self, response):
        item=ShowinfoItem()

        museum="旅顺博物馆"
        '''
        name=response.xpath("//div//text()").extract()
        print(name)
        time=response.xpath("//div/div[2]/div[4]/div/div/p[6]//text()").extract()[1]
        address=response.xpath("//div/div[2]/div[4]/div/div/p[7]//text()").extract()[1]
        introduce=response.xpath("//div/div[2]/div[4]/div/div/p[8]//text()").extract()[0]
        '''
        item['name'] = "翰林墨迹——大连、青岛两地收藏晚清名人作品展"
        item['museum'] = museum
        item['time']="2018年3月30日"
        item['address']=""
        item['introduce']="历时两年的策划与筹备，2018年3月30日，由旅顺博物馆、青岛市博物馆联合主办的《翰林墨迹——大连、青岛两地收藏晚清名人作品展》正式开展了。旅顺博物馆与青岛市博物馆都是国家一级博物馆，收藏有大量晚清名人书法作品，此次展览从两馆大量馆藏精品中选出12位晚清名家作品近百件进行展出。这12位晚清名人大都是饱学之士，翰林出身，在晚清政治、外交、教育、学术等领域各有成就，在中国近代书法史上也是举足轻重的人物。比如，王垿善大榜书，在京师时就有“无匾不是垿，无腔不是谭”的美谈，和吴郁生、刘廷琛一起被誉为青岛三大书法家；“二为帝师”的陆润庠的欧体书法清华朗润，素有盛名；康有为奠定了碑学作为一大书法流派的理论基础；罗振玉致力于古文字学研究，写甲骨文书法，临金石文字，用笔有刀刻之痕，独具风采……他们独具特色的书法风貌开创了中国近代书坛的新局面，也为大连、青岛两地留下丰厚的文化遗产，书写了两地历史文化的新篇章。大连和青岛都是近代发展起来的城市，但却不乏人文历史气息和学术气息，这与大批晚清名人在两地的文化活动是分不开的，在他们的影响下，大连与青岛逐渐形成了自身稳定的文化特质。可以说，这批晚清名人，虽身在大连与青岛，影响所及却广至中国大地，他们为近代的大连与青岛留下了大量的文化遗产，成为大连与青岛百年历史的重要组成部分。此展览将为观众提供一次欣赏晚清名人书法、品味城市历史文化的良机。《翰林墨迹——大连、青岛两地收藏晚清名人作品展》是旅顺博物馆与青岛市博物馆的首度合作，10月此展览将赴青岛市博物馆展出。 "
        yield item
