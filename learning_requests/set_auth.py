'''
使用auth参数来设置用户登录认证
给auth传入一个二元组，会默认使用HTTPBasiAuth这个类来验证
'''
import requests

r = requests.get('https://localhost:5000', auth = ('username', 'password'))
print(r.status_code)

'''
还提供了其他验证方式
如OAuth，需要安装oauth包
pip insta requests_oauthlib
详情参考文档。。。。。
'''