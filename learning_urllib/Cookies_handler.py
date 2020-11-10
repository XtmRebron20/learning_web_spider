# 学习urllib标准库
# 这是一个处理Cookies的handler实例
# 打印cookie的键和值
import http.cookiejar, urllib.request

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.zhihu.com')
for item in cookie:
    print(item.name + " = " + item.value)