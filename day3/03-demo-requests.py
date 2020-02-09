import requests
import os
url = 'https://www.baidu.com/'
response = requests.get(url)
print('服务器返回状态码{0}'.format(response.status_code))
print(response.text) 

