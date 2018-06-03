import scrapy
from ..items import ShowinfoItem

class DongbeiSpider(scrapy.Spider):

    name="dongbeiSpider"
    start_urls=['http://www.nmgbwy.com/zldt/1356.jhtml']

    def parse(self, response):

        museum="东北烈士纪念馆"

        name=response.xpath("//div/div[2]/div[4]/div/div/div/font//text()").extract()[0]
        item=ShowinfoItem()

        time=response.xpath("//div/div[2]/div[4]/div/div/p[6]//text()").extract()[1]
        address=response.xpath("//div/div[2]/div[4]/div/div/p[7]//text()").extract()[1]
        introduce=response.xpath("//div/div[2]/div[4]/div/div/p[8]//text()").extract()[0]

        item['name'] = "无声之营——沈阳二战盟军战俘营史实图片展"
        item['museum'] = museum
        item['time']=""
        item['address']=""
        item['introduce']="为充分发挥纪念馆公共文化服务职能和宣传教育阵地作用，结合深入开展“大学习、大调研、大练兵”活动安排，4月3日，由省文化厅主办，东北烈士纪念馆、沈阳“九·一八”历史博物馆联合承办的《无声之营——沈阳二战盟军战俘营史实图片展》在东北烈士纪念馆专题展厅面向社会展出，市民可免费来馆参观。"
        yield item
