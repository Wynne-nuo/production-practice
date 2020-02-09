import csv
import os
""" #写入csv文件
colums = ["姓名","年龄","电话号码"]
#写入数据
data = [("张三",21,'1355555'),
        ("李四",20,'1366666'),
        ("王二麻子",22,'1377777')]
#使用with语句打开文件关联
with open('day22/workplace/data2.csv','w',encoding='gb18030',newline='') as csvfile:
    #获取writer写入对象
    writer = csv.writer(csvfile)
    #写入数据标题行（单行
    writer.writerow(colums)
    print('标题已写入')
    writer.writerows(data)
    print('多行数据已写入') """

#读出文件
#使用with结构改造
with open('day22/workplace/data2.csv','r',encoding='utf8') as csvfile:
    #使用reader函数读取csv数据
    reader = csv.reader(csvfile)
    print('reader{0}'.format(reader))
    #使用for循环迭代reader对象
    for line in reader:
        print(line)


