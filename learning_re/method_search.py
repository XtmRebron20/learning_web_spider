'''
方法search()会在匹配时扫描整个字符串，返回第一个成功匹配的结果
正则表达式可以匹配字符串的一部分，不必与字符串完全匹配
'''
import re
content = 'Extra stings Hello 134567 World_This is a Regex Demo Extra stings'
result1 = re.match('Hello.*?(\d+).*?Demo', content)
result2 = re.search('Hello.*?(\d+).*?Demo', content)
print(result1)
print(result2)