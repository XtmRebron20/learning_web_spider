'''
使用verify参数可以控制是否验证此页面的CA证书，默认为True，会自动检测
'''
import requests

repsonse = requests.get('https://www.12306.cn', verify=False)
print(repsonse.status_code)

