'''
使用proxies参数来设置代理
支持 http://user:password@host:port 语法来设置代理
requests库还支持SOCKS协议代理，需要安装socks库
pip install 'requests[socks]'
'''
import requests

proxies = {
    'http':'http://27.206.182.205:9000',
    'https':'https://223.247.171.16:9999',
    'http':'http://user:password@host:port',
    'http':'socks://user:password@host:port',
    'https':'socks://user:password@host:port',


}

requests.get('https://taobao.com', proxies=proxies)
