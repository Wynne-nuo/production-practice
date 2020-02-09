import json
data = [{'dog':'wawa','age':'5','color':'blue'},
        {'pig':'hengheng','age':'2','color':'black'}]
strJson = json.dumps(data,ensure_ascii=False)
#测试输出
print('original data:{0}'.format(data))
print('after change:{0}'.format(strJson))

#使用json.loads函数完成json-》对象的转换
obj = json.loads(strJson)
print('obj->{0}'.format(type(obj)))
print('dog:{0}'.format(data[0]['dog']))
