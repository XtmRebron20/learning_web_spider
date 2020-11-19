'''
要使用bs4进行解析需要像xpath一样进行对象初始化
form bs4 import Beautifulsoup
soup = Beatifulsoup('HTML', 'PARSER')
'''
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>123</b></p>
<p>456</p>
<p>789</p>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml') # 不要忘记引号。可以观察到，创建解析对象的同时bs对html文档进行自动补全
print(soup.prettify()) # 格式化输出
print(soup.title.string) # 输出title标签中的字符串
print(soup.title.get_text()) # get_text()同样可以获得内容
print(soup.title) # 直接调用要选择的节点的名称就可以选择节点
print(type(soup.title)) # <class 'bs4.element.Tag'>的Tag类型,拥有string属性，返回其中的字符串
print(soup.p) # 如果有多个重复名称的标签，只会返回第一个




