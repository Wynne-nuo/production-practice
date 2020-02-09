# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#采集后数据的处理
#导包，逗号分隔值，用于存储表格数据
import csv
#导包，os模块提供了多数操作系统的功能接口函数
import os
#导包，时间类函数
import time
#导包，日志用
import logging
#继承object类的管道方法
# class DoubanmoviePipeline(object):
#     #定义一个私有类
#     def __init__(self):
#         #存放路径
#         path = 'D:\codeSavePath\production practice\DoubanMovie\TOP250.csv'
#         #存放文件格式
#         self.file = open(path,'a+',encoding='utf-8')
#         #存放文件读写格式
#         self.writer = csv.writer(self.file)
#     #pipeline必须调用的方法，返回item或dict对象
#     def process_item(self, item, spider):
#         #将item打印出来
#         print(item)
#         #打印电影排名
#         print('电影排名:{0}'.format(item['rank'][0]))
#         #按行保存
#         self.writer.writerow((item['rank'],item['name']))
#         #返回item
#         return item
#     #关闭爬虫
#     def close_spider(self,spider):
#         #调用close方法关闭
#         self.file.close() 
#     # def process_item(set,item,spider):
#     #     print('电影排名:{0}'.format(item['rank'][0]))
#     #     return item

#Json数据文件存储
#导入json库
import json
#创建一个类
class DoubanmoviePipeline(object):
    #定义私有方法来保存路径
    def __init__(self):
      #  path = 'D:\codeSavePath\production practice\DoubanMovie\JsonTOP250.json'
      #文件格式和名称以及读写规则
        self.file = open('JsonTOP250.json', 'w', encoding='utf-8')
    #运行时调用
    def process_item(self, item, spider):
        #将dict类型的数据转成str
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        #写入
        self.file.write(line)
        #返回
        return item
    #关闭爬虫的方法
    def spider_closed(self, spider):
        #调用close进行关闭
        self.file.close()

# 数据库mysql存储
#导入pymysql库
# import pymysql
# #连接数据库
# def dbHandle():
#打开数据库连接，包括用户名密码等
#     conn = pymysql.connect(
#         host = "localhost",  
#         user = "root",
#         passwd = "root",
#         charset = "utf8",
#         use_unicode = False
#     )
#返回
#     return conn
##写入数据库类
# class DoubanmoviePipeline(object):
##定义一个方法
#     def process_item(self, item, spider):
       # #写入数据库
#         dbObject = dbHandle()
       # #？？？
#         cursor = dbObject.cursor()
       # #执行sql语句
#         cursor.execute("USE test")
#         #插入数据库
#         sql = "INSERT INTO movie(rank,name) VALUES(%s,%s)"
#       抛出执行时的异常
#         try:
##执行sql语句
#             cursor.execute(sql,
#                            ( item['rank'], item['name']))
##没异常就提交到数据库
#             cursor.connection.commit()
##有异常时
#         except BaseException as e:
##给出异常的位置
#             print("错误在这里>>>>>>>>>>>>>", e, "<<<<<<<<<<<<<错误在这里")
##进行回滚
#             dbObject.rollback()
##返回
#         return item