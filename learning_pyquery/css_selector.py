'''
学习pyquery之前，先学习一下css选择器的基本语法
参考材料：https://www.w3school.com.cn/cssref/css_selectors.asp
支持css3的伪类选择器，详见css文档
'''
from pyquery import PyQuery as pq
doc = pq(filename='./learning_pyquery/demo.html')
print(doc('#container .list li'))
print(type(doc('#container .list li'))) # 仍然是PyQuery类

