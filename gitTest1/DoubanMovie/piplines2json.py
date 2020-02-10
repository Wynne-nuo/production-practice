import os
import time
class DoubanmoviePipline(object):
    def __init__(self):
        self.folder_name = 'output'
        #判断文件夹是否存在
        if not os.path.exists(self.folder_name):
            #若不存在则创建文件夹output
            os.mkdir(self.folder_name)
        print("-->JSON:writing")
        folder_name = 'output'
        #获取系统当前时间
        now = time.strftime('%Y-%m-%d',time.localtime())
        fileName = 'doubanmovietop250_'+now+'.json'
        self.file.write('[')
        pass
    #process_item（）函数，处理每一个采集到的电影数据
    def process_item(self,item,spider):
        line = json.dumps(dict(item),ensure_ascii = False)+',\n'
        self.file.write(line)
        