'''
学习requests库中的文件上传
该示例将之前爬取的github图标上传至http://httpbin.org/post站点
返回中包含了一段file字样，表示上传成功
'''
import requests

files = {
    'file':open('favicon.ico', 'rb')
}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)