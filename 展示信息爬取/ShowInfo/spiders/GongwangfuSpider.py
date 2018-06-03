import scrapy
from ..items import ShowinfoItem
import re

class GongwangfuSpider(scrapy.Spider):

    name="GongwangfuSpider"
    start_urls=["http://www.pgm.org.cn/newgwf/zxzx/list.shtml"]

    def parse(self,response):

        names=response.xpath("//div/div/div/div[2]/div[2]/ul/li/a//text()").extract()
        page_urls=response.xpath("//div/div/div/div[2]/div[2]/ul/li/a/@href").extract()
        times=response.xpath("//div/div/div/div[2]/div[2]/ul/li//text()").extract()
        l=len(names)
        museum="恭王府"
        for i in range(l):
            item=ShowinfoItem()
            item['name']=names[i].replace('\t',"")
            item['time']=times[i+3]
            item['museum']=museum
            page_url=page_urls[i].replace("../..","")
            page_url='http://www.pgm.org.cn'+page_url
            yield scrapy.Request(page_url,callback=self.parse_page,meta=item)

    def parse_page(self,response):
        item=response.meta

        content=response.xpath("//div/div/div/div[2]/div//text()").extract()
        content = ''.join(content).replace(' ', '').replace('\n', '').replace('\r', '').replace('\xa0', '').replace('\u3000e', '')
        time_str = ".*?([\u4E00-\u9FA5]+展览地点)"
        add_str=".*?([\u4E00-\u9FA5]+本次)"

        match_obj = re.match(time_str,content)
        match_obj2=re.match(add_str,content)
        if match_obj:
            time=match_obj.group().replace("展览地点","")
            item['time']=time
            if match_obj2:
                address=match_obj2.group().replace("本次","").replace(time,'')
                item['address']=address
            else:
                match_obj2=re.match(".*?([\u4E00-\u9FA5]+展览共)",content)
                address=match_obj2.group().replace(time,"").replace("展览共","")
                item['address'] = address

        introduce=response.xpath("//p//text()").extract()
        introduce=''.join(introduce).replace('\n','').replace('\r','').replace('\xa0','').replace(' ','')
        item['introduce']=introduce.replace(item['time'],"").replace(item['address'],"")
        yield item