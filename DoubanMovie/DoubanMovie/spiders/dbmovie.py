# -*- coding: utf-8 -*-
#爬虫主程序文件
#连接本地仓库和github1
#导入scrapy包
import scrapy
#导入requests包
import requests
#导入DoubanMovie items中的DoubanmovieItem
from DoubanMovie.items import DoubanmovieItem
#创建爬虫类，继承scrapy.spider类，这是最基本的类，所有编写的爬虫必须继承这个类
class DbmovieSpider(scrapy.Spider):
    #外部scrapy调用爬虫的名字
    name = 'dbmovie'
    #允许域名
    allowed_domains = ['douban.com']
    #爬取页面的起始url地址
    start_urls = ['https://movie.douban.com/top250/']
#定义parse方法，用于解析返回的数据，提取数据并生成进一步需要处理的request对象
    def parse(self, response):
        #定义当前电影信息的xpath路径
        currentPage_movie_item = response.xpath('//div[@class = "item"]')
      #循环访问数据
        for movie_item in currentPage_movie_item:
            #创建一个Movie对象
            movie = DoubanmovieItem()
            #获取电影排名并赋值rank属性
            movie['rank'] = movie_item.xpath('div[@class = "pic"]/em/text()').extract()
            #获取电影名并赋值title属性
            movie['name'] = movie_item.xpath('div[@class = "info"]/div[@class = "hd"]/a/span[@class = "title"][1]/text()').extract()
            #将封装好的一个电影信息添加到容器中
            # movie['image']=movie_item.xpath('//div[@class = "pic"]//img/@src').extract()
            # try:
            #                 #根据url下载图片
            #     pic = requests.get(movie['image'][0])
            #                 #保存图片到images文件夹
            #     with open('./images/{0}-{1}.jpg'.format(movie['rank'],movie['name'][0]), 'wb') as f:
            #         f.write(pic.content)
            #         f.flush()
            #     print("下载成功")
            # except Exception as e:
            #     print(Exception, ':', e)
            #返回，相当于return
            yield movie

    #自动请求翻页实现爬虫的深度采集
        nextPage=response.xpath('//span[@class="next"]/a/@href')
        #判断nextPage是否有效
        if nextPage:
            #拼接下一页的地址
            url=response.urljoin(nextPage[0].extract())
            #发送url后页请求
            yield scrapy.Request(url,self.parse)
