# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
#采集数据的封装实体类
import scrapy


class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #爬排名
    rank = scrapy.Field()
    name = scrapy.Field()
    image= scrapy.Field()
    pass
