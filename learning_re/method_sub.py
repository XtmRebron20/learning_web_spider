'''
sub()方法，用于替换匹配到的字符
re.sub('REGEX', 'TARGET', object)
'''
import re
content = '54aK54yr5oiR54ix5L2g'
content = re.sub('\d+', '', content) # 将所有的数字删除
print(content)