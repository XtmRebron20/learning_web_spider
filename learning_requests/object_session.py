'''
使用get()或post()请求网站时实际上是两个不同的会话
如果要维持一个会话，需要使用Session对象来请求网站
'''
import requests

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)
