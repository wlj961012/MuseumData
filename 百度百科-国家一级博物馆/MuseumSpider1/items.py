# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Museumspider1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    open_time=scrapy.Field()
    edu_activity=scrapy.Field()
    collection=scrapy.Field()
    academic=scrapy.Field()
    introduce=scrapy.Field()