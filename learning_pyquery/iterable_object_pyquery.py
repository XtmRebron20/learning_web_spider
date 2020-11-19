'''
对于PyQuery类对象来说，返回的不是列表
而是一个可迭代对象，需要用for循环解析
'''
from pyquery import PyQuery as pq
doc = pq(filename="./learning_pyquery/demo.html")
lis = doc('li').items() # 转换成生成器
print(type(lis))
print(type(doc('li')))
for li in lis:
    print(li, type(li))