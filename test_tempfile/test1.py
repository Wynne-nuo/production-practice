import tempfile
import os,sys
import csv
import time
# 时间戳生成前缀
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
# tmpdir = tempfile.mkdtemp(suffix='', prefix=now, dir='D:\codeSavePath\production practice\linshi')
aa = tempfile.TemporaryDirectory(prefix=now, dir='D:\codeSavePath\production practice\linshi')
print(aa)

# filename = "D:\codeSavePath\production practice\DoubanMovie\DoubanMovie\spiders\JsonTOP250!.json"
# with open(filename,encoding='utf-8') as fp:
#     content = fp.readlines()
    # return content,200
    # print(content)
#--------------------------
# 时间戳生成前缀
# now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
# #生成一个临时文件，指定路径改为D盘
# # aa = tempfile.TemporaryFile(mode='w+b',dir='D:',prefix=now)
# aa = tempfile.NamedTemporaryFile(mode='w+b',dir='D:',prefix=now)
# ## a = '两情若是久长时，'
# ## aa.write(a.encode('utf-8'))
# print(aa.name)
#---------------------------
# #----???已经给aa的临时文件夹更换，不知道为啥bb调用的 时候还是默认的C盘
# # bb = tempfile.gettempdir()
# # print(bb)
# # 将文件指针移到开始处，准备读取文件
# aa.seek(0)
# print(aa.read().decode('utf-8')) # 输出刚才写入的内容
# # # 关闭文件，该文件将会被自动删除
# aa.close()
    # 
    # b = '又岂在朝朝暮暮。'
    # # fp.write(a.encode('utf-8'))
    # # fp.write(b.encode('utf-8'))
    # aa.write(fp.encode())
    # fp.write(''.encode('utf-8'))

