'''
方法findall()用于获取正则表达式匹配的所有内容
区别于search()只能找到第一个匹配的内容
如果有返回结果，是列表类型，需要用遍历的方式显示
'''
import re
html = ''
result = re.findall('', html, re.S)