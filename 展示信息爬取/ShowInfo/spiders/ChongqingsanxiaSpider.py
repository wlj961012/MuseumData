import scrapy
from ..items import ShowinfoItem

class CQSXSpider(scrapy.Spider):

    name="CQSXSpider"
    start_urls=['http://www.3gmuseum.cn/web/article/toArticleNo.do?itemno=23&pageindex=1&itemsonno=25434353&articleno=40288cd560e49a0501611d8043db5fde']

    def parse(self,response):

        item=ShowinfoItem()
        museum="重庆中国三峡博物馆"
        item['museum']=museum
        name=response.xpath('//div[@class="art-dcontent"]/p[1]/span//text()').extract_first()
        item['name']=name
        time=response.xpath('//div[@class="art-dcontent"]/p[2]/span//text()').extract_first()
        item['time']=time
        address=response.xpath('//div[@class="art-dcontent"]/p[3]/span//text()').extract_first()
        item['address']=address
        introduce=response.xpath('//div[@class="art-dcontent"]/p//text()').extract()
        item['introduce']=''.join(introduce)

        yield item