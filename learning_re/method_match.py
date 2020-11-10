'''
学习match()方法
该方法传入两个参数，分别为要匹配的字符串、正则表达式
返回是否匹配
需要注意的是该方法从字符串的开头开始匹配，一旦开头不匹配，则整个字符串不匹配
match()方法更适合来检测一个字符串是否符合正则表达式的规则
该模块有两个属性
group()输出匹配到的内容
span()输出匹配的范围
'''
# import re
# content = 'Hello 123 4567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
# print(result)
# print(result.group())
# print(result.span())

'''
match()可以返回一段字符串中特定的字符
在正则表达式中将想要提取出的字符用()括起来
在调用group()时使用group(1)，可以返回第一个被括起来的正则表达式匹配的内容
同理group(2),group(3),group(4)……
'''
# import re
# content = 'Hello 1234567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('^Hello\s(\d+)\sWorld', content) # (\d+)使用括号括起的元素，表示1个或多个数字
# print(result) 
# print(result.group()) # 返回所有正则表达式匹配的内容
# print(result.group(1)) # 返回第一个被括起来的正则表达式匹配的内容
# print(result.span())

'''
使用.和*的组合匹配任意字符
.匹配任意非换行符字符
*匹配任意个之前正则表达式的字符
'''
# import re
# content = 'Hello 123 4567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('^Hello.*Demo$', content) # .*的组合可以匹配任意个非换行符字符
# print(result)
# print(result.group())
# print(result.span())

'''
贪婪与非贪婪
'''
# import re
# content = 'Hello 1234567 World_This is a Regex Demo'
# print(len(content))
# result1 = re.match('^Hello.*(\d+).*Demo$', content) # 贪婪模式，第一个.*会尽可能多的匹配字符，只留给\d+最基本的满足条件（1个）
# result2 = re.match('^Hello.*?(\d+).*Demo$', content) # 非贪婪模式，在第一个.*后加入了一个?，会尽可能少的满足第一个.*匹配字符
# result3 = re.match('^Hello.*?.Regex(.*?)', content) # 需要注意的是?表示0或1个之前表达式的匹配，使用非贪婪模式。如果放在正则表达式末尾，则会匹配0个字符，即不能匹配
# result4 = re.match('^Hello.*?.Regex(.*)', content) # 此时如果使用贪婪模式即可匹配到想要的Demo字样

# print(result1) 
# print(result1.group(1)) 
# print(result2) 
# print(result2.group(1)) 
# print(result3) 
# print(result3.group(1)) #为空
# print(result4) 
# print(result4.group(1)) #匹配到了Demo字样

'''
修饰符
较为常用的有
re.S 使.匹配包括换行符在内的所有字符
re.I 使匹配的大小写不敏感
'''
# import re 
# content ='''Hello 1234567 World_This 
# is a Regex Demo'''
# # result1 = re.match('^He.*?(\d+).*?Demo$', content)
# result2 = re.match('^He.*?(\d+).*?Demo$', content, re.S) #加入了一个参数re.S，使.包括了换行符
# # print(result1) 
# # print(result1.group(1)) 
# print(result2) 
# print(result2.group(1)) 

'''
转义匹配
当遇到使用正则表达式符号的字符时
需要在正则表达式前加入一个\来进行转义
'''
import re
content = 'www.baidu.com'
result = re.match('www\.baidu\.com', content) # 在每个.前加入\来进行转义
print(result)