'''
方法compile()，用于将正则字符串编译成正则表达式对象
方便再次使用
可以传入参数装饰符，如re.S。在使用findall(),search()等时就可以不用再传入装饰符了
'''
import re
content1 = '2020-11-09 19:19'
content2 = '2021-11-12 08:07'
content3 = '2016-12-23 12:07'
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1) # 第一个参数传入了pattern。该操作保留日期，将时间删除
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3)

