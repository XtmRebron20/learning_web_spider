'''
将字符串或流转化为Element对象后就可以使用其xpath属性了来选择需要的内容了
Element.xpath('XPATH')
'''
from lxml import etree

# 不规范的HTML文档
# html = etree.parse('./learning_lxml&xpath/test.html', etree.HTMLParser()) 
# result = html.xpath('//*')
# print(result)

# 规范的HTML文档
html = etree.parse('./learning_lxml&xpath/test2.html') 
result = html.xpath('//*')
print(result)

# 之所以使用etree.parse()方法解析 html 内容时，会报lxml.etree.XMLSyntaxError的错，
# 是因为etree.parse()默认使用的是XML的解析器，所以当html内容不规范，比如出现某个标签缺少闭合标签时，
# 就会报这个错误。这时，可使用etree.HTMLParser()创建一个HTML的解析器，然后作为etree.parse()方法的参数即可。