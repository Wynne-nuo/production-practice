from test1 import *

a = 'I love python嘿嘿'
print("复述："+ a)
print(aa.name)
aa.write(a.encode('utf-8'))
aa.seek(0)
# with open (path = aa,"r") as f:
#     for line in f:
#         print(line)

b = aa.read().decode("utf-8")
print(b)
    # print(aa.read().decode('utf-8')) # 输出刚才写入的内容
    # 关闭文件，该文件将会被自动删除
aa.close()
