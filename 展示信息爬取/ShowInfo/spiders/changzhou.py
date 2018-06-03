import scrapy
from ..items import ShowinfoItem

class changZhouSpider(scrapy.Spider):

    name="Changzhou"
    start_urls=['http://www.czmuseum.com/default.php?mod=article&do=detail&tid=20467']

    def parse(self, response):
        item=ShowinfoItem()

        museum="常州博物馆"

        name=response.xpath("//div/div[17]/div[2]/div/table/tr[1]/td//text()").extract_first()
        '''
        time=response.xpath("//div/div[2]/div[2]/div[3]/div[3]/p[2]//text()").extract()[0]
        address=response.xpath("//div/div[2]/div[2]/div[3]/div[3]/p[3]//text()").extract()[0]
        introduce=response.xpath("//div/div[2]/div[2]/div[3]/div[3]/p[3]//text()").extract()[0]
        '''
        item['name'] =name
        item['museum'] = museum
        item['time']="2018年4月12日"
        item['address']="常州博物馆一楼临时展厅"
        item['introduce']="　本次展览遴选了2016至2018年间常州金坛土墩墓群抢救性考古发掘中的重要发现，如牯牛墩土墩墓、高庄土墩墓、立夫路土墩墓群、井头村土墩墓群等。共展示文物一百五十余件（套）。展览较为详细的介绍了何为土墩墓、土墩墓的发现历史、土墩墓的类型与形制、随葬器物及主要纹饰、重要考古发现。展示文物数量丰富、内容详实、意义深刻。同时，本次展览也是江苏考古工作者面向大众推出的工作成果汇报展，将土墩墓发掘成果系统而又全面的呈现于观众面前，讲述考古发现的点点滴滴。欢迎市民朋友们走进常州博物馆，共享文物考古工作的丰硕果实。"
        yield item
