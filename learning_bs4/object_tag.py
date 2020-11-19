'''
学习TAG对象，以及运用TAG对象进行文档解析
'''
from bs4 import BeautifulSoup
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>123</b></p>
<p>456</p>
<p>789</p>
'''

'''
Tag具有的属性，以及运用这些属性获取信息
name, attrs, string
'''
soup = BeautifulSoup(html, 'lxml')

print(soup.title.name) # name属性，用来获取节点的名称
print(soup.p.attrs) # attrs属性，用来获取节点的所有属性,返回的是字典形式
print(soup.p.attrs['name']) # 当然也可以单独获取其中的一个属性
print(soup.p['name']) # 更简便的写法，同上
print(soup.p['class']) # 返回的结果有可能是列表形式，开发中应当注意类型变化
print(soup.p.string) # 获取标签内的内容

# 可以进行嵌套选择
print(soup.head.title)

# 关联选择。先选出一个节点，再根据此节点选择另外的节点。
# 使用contents属性获取直接子节点，孙节点不会单独作为列表中的一个元素。
print(soup.body.contents) # 返回的是列表形式。既包含文本。又包含节点。

# 两种返回生成器的属性 children 和 descendants
for i,child in enumerate(soup.body.children): # 返回了一个包含所以子节点的生成器
    print(i,child)  
for i,descendant in enumerate(soup.body.descendants): # 返回一个包含所有子孙节点的生成器
    print(i,descendant)

# 父节点和祖先节点
# 使用parent属性获取直接父节点，返回的是父节点以及其内部的所有内容
print(soup.p.parent)
# 使用parents属性获取祖先节点，返回的是包含所有祖先节点的生成器，用for循环解析
print(soup.p.parents)

# 兄弟节点
# 上一个兄节点和下一个弟节点
print(soup.p.previous_sibling)
print(soup.p.next_sibling)
# 所有的兄节点和所有的弟节点
print(list(soup.p.previous_siblings)) # 返回一个生成器
print(list(soup.p.next_siblings))

