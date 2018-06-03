import scrapy
from ..items import ShowinfoItem

class XiboSpider(scrapy.Spider):

    name="xiboSpider"
    start_urls=['http://www.xbpjng.cn/PlatNews/platform.aspx?c=3f80c295-81c8-49f9-838f-b3cfce9bc5c9&z=795']

    def parse(self, response):

        museum='西柏坡纪念馆'
        item=ShowinfoItem()

        '''names = response.xpath("//*[@id='ctl00']/div[2]/div/div[2]/h2[1]/a").extract()
        page_urls = response.xpath("//div[@class='all-content']/h2/a/@href").extract()
        times = response.xpath("//div[@class='rt']//text()").extract()

        l=len(names)
        print(names)
        for i in range(l):
            item = ShowinfoItem()
            name = names[i]
            page_url = page_urls[i]
            time = times[i]
            item['name'] = name
            item['time'] = time
            item['museum'] = museum
            item['address'] = museum
            page_url = 'http://www.xbpjng.cn' + page_url

            yield scrapy.Request(page_url, callback=self.parse_page, meta=item)'''

        item=ShowinfoItem()
        item['museum']=museum
        item['address']=museum
        item['time']='2017/6/30 0:00:35'
        item['name']='“寻找最美秋天”携手行活动优秀作品展开展'
        item['introduce']='12月26日，“寻找最美秋天” 携手行活动优秀作品展在西柏坡陈列展览馆开展为推进我馆“两学一做”学习教育深入开展，确保学到深处、学到实处，突出“创新动作”有特色，同时丰富广大干部职工的精神文化生活，激发爱馆、爱事业、爱自然、爱生活的热情，经馆党委研究决定，由馆“两学一做”学习教育办公室和工会牵头，在全馆范围内开展了“寻找最美秋天”携手行活动。同志们积极参与，奉献了一大批优秀作品，共征集到79位干部职工的165幅作品,经过评委会严格打分,共评选出优秀作品28幅,其中诗歌散文14篇,摄影作品14幅。秋之美景在眼中,更在心中。在此次寻找最美秋天活动中,广大干部职工通过诗歌、散文、摄影等多种形式表达了对金色秋天的美好感受和对幸福生活的向往,虽不及名家之作,却也令人赏心悦目。通过此次展览进一步增强了广大干部职工干事创业的激情,凝聚起了团结奋进、积极向上的正能量。'
        yield item
