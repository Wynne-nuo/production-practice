import flask,json
from flask import request

server=flask.Flask(__name__)

@server.route('/',methods=['get','post'])#只有在函数前加上@server.route (),这个函数才是个接口，不是一般的函数
def reg():
    dict = {}
    idcard = request.values.get('userid')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
    }
    url = 'http://qq.ip138.com/idsearch/index.asp?userid=211302199803141625&action=idcard&userid={}'.format(idcard)

    r = requests.get(url,headers=headers)
    # print(r.content.decode('gbk'))
   # a = re.findall('发证地：</td><td class="tdc2">(.*?)<br/></td></tr>',r.content.decode('gbk'))
    a = re.findall('发证地：</td><p><br></p></td></tr>',r.content.decode('gbk'))
    if a == []:
        dict['idcard'] = idcard
        dict['area'] = ''
        return json.dumps(dict, ensure_ascii=False)
    else:
        dict['idcard'] = idcard
        dict['area'] = a[0]
        return json.dumps(dict,ensure_ascii=False)

server.run(port=8888,debug=True,host='0.0.0.0')
