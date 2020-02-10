# -*- coding: utf-8 -*-
import scrapy
import requests

from DoubanMovie.items import DoubanmovieItem
class DbmovieSpider(scrapy.Spider):
    name = 'dbmovie'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250/']

    def parse(self, response):
        currentPage_movie_item = response.xpath('//div[@class = "item"]')
      
        for movie_item in currentPage_movie_item:
            #创建一个Movie对象
            movie = DoubanmovieItem()
            #获取电影排名并赋值rank属性
            movie['rank'] = movie_item.xpath('div[@class = "pic"]/em/text()').extract()
            #获取电影名并赋值title属性
            movie['name'] = movie_item.xpath('div[@class = "info"]/div[@class = "hd"]/a/span[@class = "title"][1]/text()').extract()
            #将封装好的一个电影信息添加到容器中
          
            movie['image']=movie_item.xpath('//div[@class = "pic"]//img/@src').extract()
            
            try:
                            #根据url下载图片
                
                pic = requests.get(movie['image'][0])
                            #保存图片到images文件夹
                
                with open('./images/{0}-{1}.jpg'.format(movie['rank'],movie['name'][0]), 'wb') as f:
                    f.write(pic.content)
                    f.flush()
                print("下载成功")
            except Exception as e:
            
                print(Exception, ':', e)
            yield movie

    #自动请求翻页实现爬虫的深度采集
        # nextPage=response.xpath('//span[@class="next"]/a/@href')
        #       #判断nextPage是否有效
        # if nextPage:
        #           #拼接下一页的地址
        #     url=response.urljoin(nextPage[0].extract())
        #         #发送url后页请求
        #     yield scrapy.Request(url,self.parse)
       

        


#根据电影海报url地址下载图片



