'''
Response对象有许多属性：
text, content, status_code, headers, cookies, url, history, code(用于查询状态码)
'''
import requests
r = requests.get('https://www.jianshu.com')
print('text属性：', type(r.text), r.text)
print('content属性：', type(r.content), r.content)
print('status_code属性：', type(r.status_code), r.status_code)
print('headers属性：', type(r.headers), r.headers)
print('cookies属性：', type(r.cookies), r.cookies)
print('url属性：', type(r.url), r.url)
print('history属性：', type(r.history), r.history)
