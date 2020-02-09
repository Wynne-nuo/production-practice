import json
import os
""" #写入json
filePath = ('day22/workplace/json-dump.json')
data = {'cat':'cute','name':'mimi'}
json.dump(data,open(filePath,'w'))
print('已写入workplace的json-dump.json') """
#读取
with open('day22/workplace/json-dump.json','r',encoding='utf8') as fp:
    #dump函数写入json数据
    data = json.load(fp)
    print('data{0}'.format(type(data)))
    for line in data:
        print(line)
    pass