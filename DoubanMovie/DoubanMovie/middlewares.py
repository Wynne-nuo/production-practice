# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

#导包
from scrapy import signals
#用于插入自定义功能的中间件
class DoubanmovieSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    #定义入口类方法，接受一个crawler实例，使自己可以访问setting等文件
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s
    #爬虫需处理的每个响应，都会调用此方法，两个参数：resp是正在处理的响应
    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        #返回none，则继续处理响应并执行其他中间件
        return None
    #处理响应后，从返回的结果中调用output方法
    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.
        # Must return an iterable of Request, dict or Item objects.
        #结果必须返回request、item或dict
        for i in result:
            #结束
            yield i
    #产生异常时调用的方法
    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        #结束
        pass
    #与output方法类似，但必须返回可迭代对象
    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        #必须仅返回一个request
        for r in start_requests:
            #结束
            yield r
    #通过singal连接到信号并在打开spider程序后发送信号
    def spider_opened(self, spider):
        #返回一个日志信息 已经打开：X爬虫程序
        spider.logger.info('Spider opened: %s' % spider.name)

#继承object的下载时的自定义类
class DoubanmovieDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    #创建一个中间件实例
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        #创建一个实例对象
        s = cls()
        #通过singal连接到信号并在打开spider程序后发送信号
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        #返回实例s
        return s
    #调用每一个通过下载的请求
    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        #返回none
        return None
    #响应从下载器返回的请求
    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        #返回响应
        return response
    #当下载出现异常时
    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        #结束
        pass
    #通过singal连接到信号并在打开spider程序后发送信号
    def spider_opened(self, spider):
        #返回一个日志信息 已经打开：X爬虫程序 
        spider.logger.info('Spider opened: %s' % spider.name)
