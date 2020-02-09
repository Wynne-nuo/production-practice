import pickle
import os
#定义一个列表
a = [1,2,3,'abc']
print('原始数据',end = ' ')
#序列化
data1 = pickle.dumps(a)
print('序列化数据',end = ' ')
print(data1)
#反序列化
data2 = pickle.loads(data1)
print('反序列化数据',end = ' ')
print(data2)