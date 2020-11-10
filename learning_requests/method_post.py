'''
这是一个请求httpbin.psot的例子
若为post请求，网站会把相关信息返回回来
'''
import requests
data = {
    'name':'xby',
    'age':'24',
}
r = requests.post('http://httpbin.org/post', data=data)
print(r.text)
