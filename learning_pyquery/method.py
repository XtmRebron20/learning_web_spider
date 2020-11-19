'''
pyquery类中定义了许多方法
'''
from pyquery import PyQuery as pq
doc = pq(filename="./learning_pyquery/demo.html")
# find()方法,查找该节点的子孙节点
print(doc('.list').find('li')) # 在具有list类的子孙元素查找：具有li名字的元素
# children()方法，查找该节点的子节点
print(doc('#container').children('.list')) # 在具有container的id的子孙元素查找：具有list类的元素

# 同理parent()，查找该节点的直接父元素
# parents()，查找该节点的祖先元素

# 使用sibling()，查找该节点的所有兄弟元素

# 获取元素的属性，attr()
a = doc('.item-0.active a')
print(a, type(a))
print(a.attr('href'))
# 或者另一种写法.attr.ATTRIBUTE
print(a.attr.href)
print('\n')
# 若选中多个元素时，想要获得它们的属性则需要用到item()遍历
# 遍历详见iterable_object_pyquery.py文件
a2 = doc('a')
print(a2.attr('href')) # 只会提取出第一个a元素的属性
for i in a2.items(): # 遍历可以提取出所有a的属性
    print(i.attr('href'))
print('\n')

# text()方法可以获取文本，只保留文本，标签全部去除
print(a.text())
# 若还想包括HTML标签文本，可以使用html()方法
print(a.html())
# 对于选中多个元素而言，text()和html()的处理方式不同
# text()会将内部的所有文字保留，形成一个字符串返回，用空格间隔开
print(a2.text())
# 但是html()需要用遍历法来进行解析
for i in a2.items():
    print(i.html())

'''
pyquery还有许多方法，可以达到修改html文本的目的
'''
# addClass, removeClass 添加类名和删除类名
li = doc('.item-0.active')
print(li)
li.removeClass('active')
print(li)
li.addClass('activate')
print(li)
print('\n')

# attr(),text(),html()方法可以替换检索到的内容
li.attr('name', 'link') # 替换属性，第一个参数为属性名，第二个参数为属性值
print(li)
li.text('have been changed') # 直接传入要修改成的字符串
print(li)
li.html('<span>changed</span>') # 传入要修改的标签及其内容
print(li)

# remove()方法，直接删除该元素。在信息提取时非常有用。
li.find('span').remove() # 直接删除了span元素
print(li)

# 还有更多方法如：append(),empty(),prepend()等。其用法和jQuery完全一致。
