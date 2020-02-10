from flask import Flask,g
from flask_restful import reqparse, abort, Api, Resource
import requests
import os,sys,subprocess
from  subprocess import Popen,PIPE,run
from scrapy import cmdline
import scrapy,shlex,re,tempfile,logging,json,tempfile,time,csv,tempfile
from time import sleep

##test1
# print("----------this is api.py-------------------")
# sys.path.append(r'D:\codeSavePath\production practice\DoubanMovie\DoubanMovie')
# import main,pipelines
# sys.path.append(r'D:\codeSavePath\production practice\DoubanMovie\DoubanMovie\spiders')
# import dbmovie
# sys.path.append(r'D:\codeSavePath\production practice\DoubanMovie')
# import DoubanMovie
# sys.path.append(r'D:\codeSavePath\production practice')
# import DoubanMovie

# from DoubanMovie.DoubanMovie.spiders.dbmovie import *
# import DoubanMovie.DoubanMovie
# import sys
# sys.path.append("../")
# import DoubanMovie.DoubanMovie.main

# import DoubanMovie.DoubanMovie.spiders.dbmovie
# sys.path.append("../..")
# import DoubanMovie.DoubanMovie.items



app = Flask(__name__)   
api = Api(app)
TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}
# 查看id是否存在于todos中，存在不做动作，如果不在，提示错误信息
def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))
#library提供的解析用户请求

parser = reqparse.RequestParser()  ##
parser.add_argument('task')
# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]
    


    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        #解析参数
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201
        
class ToTest(Resource):
    def get(self):
        #加参数，比如num，是用户传进来的，然后把num传到爬虫里
        #需crawl 并返回文件
        #加绝对路径
        # #--------创建临时文件夹tempfile(不可行，调不到aa)
        # now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
        # aa = tempfile.mkdtemp(suffix='', prefix=now, dir='D:') #临时文件夹
        # # aa = tempfile.TemporaryFile(suffix='', prefix=now, dir='D:')#临时文件
        # print(aa)
        # str(aa)
        # print(aa)

        # print(aa)
        # 时间戳生成前缀
        # now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
        #生成一个临时文件，指定路径改为D盘
        # aa = tempfile.TemporaryFile(mode='w+b',dir='D:',prefix=now)
        # # aa = tempfile.NamedTemporaryFile(mode='w+b',dir='D:',prefix=now,suffix='.json')
        # bb = tempfile.TemporaryDirectory(prefix=now, dir='D:\codeSavePath\production practice\linshi')
        # print("-----这是api中的临时文件-------")
        # print(bb.name)

        # p = subprocess.Popen("scrapy runspider --loglevel=INFO dbmovie.py", shell=True)
        #-------cwd 指定绝对路径调用爬虫（可行）
        p = Popen('scrapy runspider --loglevel=INFO dbmovie.py',shell= True,stdout=PIPE,stderr=PIPE,cwd='D:\\codeSavePath\\production practice\\DoubanMovie\\DoubanMovie\\spiders')
        # p = Popen('scrapy runspider --loglevel=INFO dbmovie.py -a FILE_NAME = aa',shell= True,stdout=PIPE,stderr=PIPE,cwd='D:\\codeSavePath\\production practice\\DoubanMovie\\DoubanMovie\\spiders')
        # p = Popen('scrapy crawl dbmovie -a file_name=aa',shell= True,stdout=PIPE,stderr=PIPE,cwd='D:\\codeSavePath\\production practice\\DoubanMovie\\DoubanMovie\\spiders')
        p.wait()
        print(p.stdout.readlines())
        print(p.stderr.readlines())
        #---------直接读取文件（可行
        # filename = aa
        # with open(filename,encoding='UTF-8') as fp:
        #     content = fp.readlines()
        #     return content,200
        #利用临时文件读取(不可行)
        # aa.seek(0)
        # print(aa.read())
        # aa.close()
        # ------以读取文件形式输出到终端（可行）
        filename = "D:\codeSavePath\production practice\DoubanMovie\DoubanMovie\spiders\JsonTOP250.json"
        with open(filename,encoding='UTF-8') as fp:
            content = fp.readlines()
            return content,200
            # print(content)
            ##return json.load(fp)   #这样输出json文件太大，无法读取

        #-------run方法输出到终端，能运行，但是结果返回的是随机浏览器的代码，不知道为什么
        # p = subprocess.run('pushd "D:\codeSavePath\production practice\DoubanMovie\DoubanMovie\spiders" ; scrapy runspider --loglevel=INFO dbmovie.py ; popd',shell= True,stdout = subprocess.PIPE,stderr = subprocess.PIPE)
        # a = subprocess.run('scrapy runspider --loglevel=INFO dbmovie.py',shell= True,stdout = subprocess.PIPE,stderr = subprocess.PIPE,cwd='D:\codeSavePath\production practice\DoubanMovie\DoubanMovie\spiders')
        # assert a.returncode ==0,a.stderr.decode("utf-8")
        # assert a.returncode ==0
        # return a.stdout.decode("utf-8")
        #------临时文件
        # now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
        # aa = tempfile.TemporaryFile(mode='w+b',dir='D:',prefix=now)
        # bb = aa.write(p.stdout)
        # print(aa.name)
        # return bb

        
        
        
        #------相对路径调用爬虫（不可行）
        # p = Popen('scrapy runspider --loglevel=INFO dbmovie.py',shell= True,stdout=PIPE,stderr=PIPE)
        # p.wait()
        #-------communicate输出倒终端(不行)
        # p.communicate()
        # return p.stdout.read().decode("utf-8")
        #-------tempfile输出倒终端(不行)
        # with tempfile.TemporaryFile() as tempf:
        #     p = Popen('scrapy runspider --loglevel=INFO dbmovie.py',shell= True,stdout=tempf,stderr=PIPE,cwd='D:\\codeSavePath\\production practice\\DoubanMovie\\DoubanMovie\\spiders')
        #     p.wait()
        #     tempf.seek(0)
        #     print (tempf.read())
        #--------popen.stout输出到终端（不行）
        # pipe = Popen("scrapy runspider --loglevel=INFO dbmovie.py", shell=True, stdout=PIPE,cwd='D:\\codeSavePath\\production practice\\DoubanMovie\\DoubanMovie\\spiders').stdout
        # output = pipe.read()
        #-------shlex 调用爬虫(不行)
        # shell_cmd = 'scrapy runspider --loglevel=INFO dbmovie.py'
        # cmd = shlex.split(shell_cmd)
        # p = subprocess.Popen(cmd,shell= True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,cwd='D:\\codeSavePath\\production practice\\DoubanMovie\\DoubanMovie\\spiders')
        

        #-------cmdline调用爬虫（不可行）
        # cmdline.execute('scrapy crawl dbmovie'.split())
        # args = "scrapy crawl dbmovie".split()
        # cmdline.execute(args)
        #-------scrapy调用爬虫（不可行）
        # subprocess.Popen("scrapy crawl dbmovie", shell=True)
        #-------subprogress.popen绝对路径调用爬虫（不可行）
        # p = subprocess.Popen('pushd "D:\\codeSavePath\\production practice\\DoubanMovie\\DoubanMovie\\spiders" ; scrapy runspider --loglevel=INFO dbmovie.py ; popd', shell=True)
        
        #-------用以前的scrapy crawl命令看看可不可以直接输出到终端(不行)
        # p = Popen('scrapy scawl dbmovie',shell= True,cwd='D:\\codeSavePath\\production practice\\DoubanMovie')
        # p.wait()
        # print(p)
        #-------print输出到终端（不可行）
        # print(p)
        #-------popen标准输出到终端（不可行）
        # if (p.returncode == 0):
        #     print("stdout%s:" %p.stdout.read())
        # print("wynne太难了")
       
        # return 'fail',500
    #运行有错：说是换行的错误，但不知道错在哪
    # def run_command(cmd):
    #     cmd = 'scrapy runspider --loglevel=INFO dbmovie.py'
    #     p = subprecess.Popen(cmd,shell= True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,cwd='D:\\codeSavePath\\production practice\\DoubanMovie\\DoubanMovie\\spiders')
    #     p.wait()
    #     for line in iter(p.stdout.readline,b''):
    #         if line:
    #             yield line
    #     while p.poll() is None:
    #         sleep(.1)
    #     err = p.stderr.read()
    #     if p.returncode !=0:
    #         print("error:"+str(err))
    #     for line in run_command(cmd):
    #         return line

# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    #get只读，不改变状态
    def get(self):
        return TODOS
    #post可能会改变状态
    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201
##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')   ##
api.add_resource(Todo, '/todos/<todo_id>')

api.add_resource(ToTest,'/crawl')

# api.add_resource(Test_main,'/test_main')
# if __name__ == '__main__':
#     app.run(debug=True)
    # sc = Test_main()
    # result = sc.get()
    # print("result:",result)