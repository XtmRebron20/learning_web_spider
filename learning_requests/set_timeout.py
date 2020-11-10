'''
使用timeout参数来设置超时时间
此时间为连接(connect)和读取(read)两步骤的时间总和
如果要指定二者的时间可以用元祖传入，timeout = (1,2)
如果想要永久等待可以设置为None或者不设置留空（默认为None）
'''
import requests

r = requests.get('https://www.baidu.com', timeout = 0.001)
print(r.status_code)
