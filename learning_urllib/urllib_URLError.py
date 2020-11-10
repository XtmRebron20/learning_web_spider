# 学习urllib标准库中error模块
# 这是一个打开一个未知页面的脚本
# 用于学习URLError类的reson属性
# 标准库：urllib    模块：error     类：URLError
# 继承自OSError类（error异常模块的基类）
# from urllib import request, error
try:
    response = request.urlopen('https://cuiqingcai.com/index.html')
except error.URLError as e:
    print(e.reason)

# 标准库：urllib    模块：error     类：HTTPError
# 继承自URLError类
# from urllib import request, error
# try:
#     response = request.urlopen('https://cuiqingcai.com/index.html')
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep='\n')
