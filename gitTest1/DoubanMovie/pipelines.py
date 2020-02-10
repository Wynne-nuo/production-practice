# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#采集后数据的处理
import csv
import os
import time
import logging
class DoubanmoviePipeline(object):
    def __init__(self):
        path = 'D:\codeSavePath\production practice\DoubanMovie\TOP250.csv'
        self.file = open(path,'a+',encoding='utf-8')
        self.writer = csv.writer(self.file)
    def process_item(self, item, spider):
        print(item)
        print('电影排名:{0}'.format(item['rank'][0]))
        self.writer.writerow((item['rank'],item['name']))
        return item
    def close_spider(self,spider):
        self.file.close() 
    # def process_item(set,item,spider):
    #     print('电影排名:{0}'.format(item['rank'][0]))
    #     return item

#Json数据文件存储
# import json
# class DoubanmoviePipeline(object):
#     def __init__(self):
#       #  path = 'D:\codeSavePath\production practice\DoubanMovie\JsonTOP250.json'
#         self.file = open('JsonTOP250.json', 'w', encoding='utf-8')
#     def process_item(self, item, spider):
#         line = json.dumps(dict(item), ensure_ascii=False) + "\n"
#         self.file.write(line)
#         return item
#     def spider_closed(self, spider):
#         self.file.close()

#数据库mysql存储
# import pymysql
# #连接数据库
# def dbHandle():
#     conn = pymysql.connect(
#         host = "localhost",
#         user = "root",
#         passwd = "root",
#         charset = "utf8",
#         use_unicode = False
#     )
#     return conn

# class DoubanmoviePipeline(object):
#     def process_item(self, item, spider):
#         dbObject = dbHandle()
#         cursor = dbObject.cursor()
#         cursor.execute("USE test")
#         #插入数据库
#         sql = "INSERT INTO movie(rank,name) VALUES(%s,%s)"
#         try:
#             cursor.execute(sql,
#                            ( item['rank'], item['name']))
#             cursor.connection.commit()
#         except BaseException as e:
#             print("错误在这里>>>>>>>>>>>>>", e, "<<<<<<<<<<<<<错误在这里")
#             dbObject.rollback()
#         return item
