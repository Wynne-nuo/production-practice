import csv
""" #写入csv数据
data = [{'first row':'111','second row':'222'}]
#读取csv数据并转成字典数据类型
with open('day22/workplace/data1.csv','w',newline='') as csvfile:
    #获取key值部分
    keys = [k for k in data[0]]
    print(keys)
    #使用DictWriter（）函数读取csv数据
    writer = csv.DictWriter(csvfile,fieldnames = keys)
    #调用writeheader写入数据标题
    writer.writeheader()
    print('标题已写入')
    #遍历数据
    for d in data:
        writer.writerow(d)
    print('数据已写入') """


 #读取csv数据（不能跟写入一起运行       ！！！！！有错
def getCSV():
    #读取csv数据并转成字典数据类型
    with open('day22/workplace/data1.csv','r') as csvfile:
        #使用DictWriter（）函数读取csv数据
        reader = csv.DictReader(csvfile)
        print('read{0}'.format(reader))
        #返回数据
        for i in reader:
            print(dict(i))
            print('已读出')
        return[dict(line) for line in reader]
    #函数调用
print(getCSV())       