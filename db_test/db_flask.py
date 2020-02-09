import flask,json
from flask import request

server=flask.Flask(__name__)#__name__代表当前的python文件。把当前的python文件当做一个服务启动

@server.route('/',methods=['get','post'])#只有在函数前加上@server.route (),这个函数才是个接口，不是一般的函数
def reg():
    dict = {}
    name = request.values.get('userid')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
    }
    url = 'https://movie.douban.com/top250/'.format(name)

    r = requests.get(url,headers=headers)
    # print(r.content.decode('gbk'))
    #a = re.findall('div[@class = "pic"]/em/text()',r.content.decode('gbk'))
    a = re.xpath('div[@class = "info"]/div[@class = "hd"]/a/span[@class = "title"][1]/text()').extract()
    if a == []:
        dict['name'] = name
        #dict['area'] = ''
        return json.dumps(dict, ensure_ascii=False)
    else:
        dict['name'] = name
        #dict['area'] = a[0]
        return json.dumps(dict,ensure_ascii=False)

server.run(port=5000,debug=True,host='0.0.0.0')
