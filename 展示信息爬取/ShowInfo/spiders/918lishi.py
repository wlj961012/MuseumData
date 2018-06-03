import scrapy
from ..items import ShowinfoItem

class BeijingSpider(scrapy.Spider):

    name="918Spider"
    start_urls=['http://www.nmgbwy.com/zldt/1356.jhtml']

    def parse(self, response):
        item=ShowinfoItem()

        museum="“九·一八”历史博物馆"
        '''
        name=response.xpath("//div//text()").extract()

        time=response.xpath("//div/div/div/div[1]/div/div[2]/div/div[1]/div[2]/div[2]/span[1]//text()").extract()
        print(time)

        address="沈阳“九·一八”历史博物馆"
        introduce=response.xpath("//div/div/div/div[1]/div/div[2]/div/div[1]/div[2]/div[3]/p[2]//text()").extract()
        '''
        item['name'] = "飞虎群英——二战美军飞虎队援华抗日纪实图片展"
        item['museum'] = museum
        item['time']="4月28日"
        item['address']="沈阳“九·一八”历史博物馆"
        item['introduce']="该展览依据美籍华侨陈灿培博士原创展览《向二战援华飞虎群英致敬》英文版为基础，其中包括罗斯福的“秘密命令”、飞虎队的组织、总司令陈纳德、美志愿军第一大队、援华特遣队、第14航空队、华人飞虎队员、中美空军联队、血符、飞虎队队员奖章、向飞虎队致谢、向中美友谊致敬、中国领导人与飞虎队、美飞虎队及援华部分单位徽章和纪念品、中国纪念陈纳德和飞虎队的邮票15个单元，通过200余张珍贵的历史照片，概括介绍二战期间美军飞虎队援华抗日的历史。"
        yield item
