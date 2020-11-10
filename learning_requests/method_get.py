''' 
一个查看get()方法返回的Response实例
'''
# import requests
# r = requests.get('https://www.baidu.com')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)

'''
使用get()方法请求连接 http://httpbin.org/get
该网站会判断客户端是否发起get请求
get可以接收一个params变量
返回的类型实际上是str类型，并且是json格式的
'''
# import requests
# data = {
#     'name':'xby',
#     'age':'24'
# }
# r = requests.get('http://httpbin.org/get', params=data)
# print(r.text)
# print(r.json())

'''
这是一个抓取 知乎、发现页面的例子
'''
# import requests
# import re
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#     'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 '
#     'Safari/537.36',   
# }
# r = requests.get('https://www.zhihu.com/explore', headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# tittles = re.findall(pattern, r.text)
# print(tittles)

'''
正是一个抓取github站点图标的例子
用于展示抓取二进制数据并保存
'''
import requests
r = requests.get('https://www.github.com/favicon.ico')
# print(r.text)
# print(r.content)
with open('favicon.ico', 'wb') as f:
    f.write(r.content)