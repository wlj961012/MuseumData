import scrapy
from ..items import ShowinfoItem


class LuxunSpider(scrapy.Spider):

    name="luxunSpider"
    start_urls=['http://www.luxunmuseum.com.cn/zhanlan/zhanlanhuigu/']

    def parse(self,response):

        museum = "北京鲁迅博物馆"
        content=response.xpath("//div[@class='list_cl r']/dt/a/text()").extract()
        page_urls=response.xpath("//div[@class='list_cl r']/dt/a/@href").extract()

        if content:
            l=len(content)
            for i in range(l):
                item=ShowinfoItem()
                item['name']=content[i]
                item['museum']=museum
                page_url='http://www.luxunmuseum.com.cn'+page_urls[i]
                yield scrapy.Request(page_url,callback=self.parse_content,meta=item)
        next_page=response.xpath('//p[@class="xiaye"]/a/@href').extract_first()
        if next_page:
            next_page='http://www.luxunmuseum.com.cn/zhanlan/zhanlanhuigu/'+next_page
            yield scrapy.Request(next_page,callback=self.parse)

    def parse_content(self,reponse):

        item=reponse.meta
        content=reponse.xpath("//div[@class='content_nr']//text()").extract()
        if content:
            item['introduce']=''.join(content).replace('\n','').replace('\t',"").replace('\r',"").replace('\xa0',"").replace(" ","")
        time_add=''.join(reponse.xpath("//div[@class='content_nr']/div[2]/div[1]//text()").extract()).replace('\n','').replace('\t',"").replace('\r',"").replace('\xa0',"").replace(" ","")
        if not time_add:
            time_add=''.join(reponse.xpath("//div[@class='content_nr']/div[2]//text()").extract()).replace('\n','').replace('\t',"").replace('\r',"").replace('\xa0',"").replace(" ","")
            if not time_add:
                if content:
                    time_add=''.join(content).replace('\n','').replace('\t',"").replace('\r',"").replace('\xa0',"").replace(" ","")
        item['time']=time_add
        item['address']=time_add
        yield item

