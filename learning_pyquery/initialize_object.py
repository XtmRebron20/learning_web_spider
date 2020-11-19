'''
使用pyquery中的PyQuery类来初始化对象
'''
html = '''
<div>
<ul>first item
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">03 item</a></li>
<li class="item-1 active"><a href="link4.html">04 item</a></li>
<li class="item-0"><a href="link5.html">05 item</a></li>
</ul>
</div>
'''
from pyquery import PyQuery as pq
# 使用字符串来进行初始化，不需要指定参数名
doc = pq(html)
print(doc('li')) # 选择了所有li节点

# 可以将url作为参数传给PyQuery类来进行初始化,需要指定参数名为url
doc2 = pq(url="https://cuiqingcai.com")
print(doc2('title'))

# 还可以将本地文件作文参数进行初始化，需要指定参数名为filename
doc3 = pq(filename="./learning_pyquery/demo.html")
print(doc3)