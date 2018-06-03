# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider, Request
import requests
import lxml.html
from ..items import ShowinfoItem

class QingzhoumuseumSpider(scrapy.Spider):
    name = 'qingzhoumuseum'
    start_urls = ['http://www.qzbowuguan.com/news_view.asp?newsid=1621']
    museum="青州博物馆"

    def parse(self, response):
        # res=response.xpath('//div[@class="row zl_list"]/div[@class="col-xs-12 col-md-4"]')

        # for each in res:

            # name=each.xpath('//div[@class="zl_text"]/h4/text()').extract()
            # url=each.xpath('div[@class="caption"]/a/@href').extract()
            # url=''.join(url)
            # html = requests.get(url).content
            # selector = lxml.html.document_fromstring(html)
            # introduce=selector.xpath('//div[@class="hd_nr"]/p/text()')
            # introduce=''.join(introduce)

            time="2018-5-1"

            address="青州博物馆"

            name="青州市书画家协会迎“五一”书画展暨名家邀请展"

            introduce="4月23日上午，青州市书画家协会迎“五一”书画展暨名家邀请展在青州市博物馆隆重开幕。展览由青州市书画家协会主办、青州市博物馆协办。此次展览特别邀请了山东省国画院院长、中国美协理事朱全增、青州市书画界领导及书画名家出席开幕式。本次展览汇集了青州市书画家协会会员及市内外书画名家的精品近作100余幅，艺术家们用笔墨抒写时代、用丹青讴歌盛世，参展作品灵动秀美、遒劲厚重、端庄内敛、大气磅礴，是我市“五一”期间献给广大观众的一份精神厚礼，也将为我市繁荣发展的文化事业增添一道亮丽的风景。"

            item=ShowinfoItem()
            item['museum']=self.museum
            item['name']=name
            item['time']=time
            item['address']=address
            item['introduce']=introduce

            yield item







