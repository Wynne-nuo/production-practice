# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

#采集数据的封装实体类
#导包
import scrapy
#继承scrapy.Item类的DoubanmovieItem类
class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #爬排名
    rank = scrapy.Field()
    #爬名字
    name = scrapy.Field()
    #爬图片
    #image= scrapy.Field()
    #空语句，保持结构完整
    pass
