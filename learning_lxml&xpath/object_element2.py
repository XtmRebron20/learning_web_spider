'''
整理xpath语法，详情查看：https://www.w3school.com.cn/xpath/xpath_syntax.asp
'''
from lxml import etree

html = etree.parse('./learning_lxml&xpath/test2.html', etree.HTMLParser()) 

# 选取所有节点//*
result1 = html.xpath('//*')

# 选取所有指定名字的节点//nodename
result2 = html.xpath('//li')

# 选取指定父节点的子节点//pre-nodename/nodename
result3 = html.xpath('//div/ul')

#选取指定父节点的子孙节点//pre-nodename//nodename
result4 = html.xpath('//div//*')

print(result1, '\n' , result2, '\n', result3, '\n', result4)
'''
总结：//表示关注子孙节点，/表示只关注子节点。*表示全部节点。
'''

# 先选中href属性为link-4.html的a节点，然后获取其父节点，然后获取其class属性
# 获取其属性时直接@class，需要属性作为匹配规则时需要加上括号[@class=“”]
result5 = html.xpath('//a[@href="link-4.html"]/../@class')
# 或者写成parent::*同样表示其父节点
result6 = html.xpath('//a[@href="link-4.html"]/parent::*/@class')

print(result5,result6)

# 使用[@class="item-0"]来获取拥有class="item-0"的元素，
# 使用[@class=]来获取拥有class的元素
result7 = html.xpath('//li[@class="item-0"]')
result8 = html.xpath('//li[@class]')
print(result7)
print(result8)

# 使用text()方法来获取标签下的文本
# 下面这个例子获取的是<li>节点中的各元素，并不是<a>节点中的。所以返回来一个\n（自动补全的换行符）
result9 = html.xpath('//li[@class="item-0"]/text()')
print(result9)
# 若要正确选中a标签下的文本需要这样写
result10 = html.xpath('//li[@class="item-0"]/a/text()')
# 或者
result11 = html.xpath('//li[@class="item-0"]//text()')
print(result10, result11)

# 获取节点的属性@属性名。
# 注意区别于[@属性名]：用于选择属性。并非获取属性。
result12 = html.xpath('//li/a/@href')
print(result12)

# 属性名中有多个值时需要用contain()方法，例如
text = '<li class="a b c"></li>'
# 当需要查找名为class的属性中的a值时
result13 = html.xpath('//li[contain(@calss,"li")]')
# 第一个参数为属性名，第二个参数为属性值

# 当需要同时匹配多个条件时用and连接
text2 = '<li class="a b c" name="item"></li>'
result14 = html.xpath('//li[contain(@class,a) and @name="item"]')

# 运算符的引入，详见书165页，表4-2。或者：https://www.w3school.com.cn/xpath/xpath_operators.asp

# 按照一定的顺序提取元素
# xpath内置100多种函数，其中运用上下文函数可以达到按照一定顺序查找元素的目的
# 了解更多函数：https://www.w3school.com.cn/xpath/xpath_functions.asp
result15 = html.xpath('//li[1]/a/text()') # 获取第一个li中a的文本（序号以1开头而不是索引0）
result16 = html.xpath('//li[last()]/a/text()') # 获取最后一个li中a的文本
result17 = html.xpath('//li[position()<3]/a/text()') # 获取位置小于三的li中a的文本（也就是前两个）
result18 = html.xpath('//li[last()-2]/a/text()') # 获取倒数第三个li中a的文本（last是最后一个，所以-2就是倒数第三个）

# 节点轴选择
# 节点轴：理解为当前节点的节点集合
# 轴名称	                         结果
# ancestor	                        选取当前节点的所有先辈（父、祖父等）。
# ancestor-or-self	                选取当前节点的所有先辈（父、祖父等）以及当前节点本身。
# attribute	                        选取当前节点的所有属性。
# child	                            选取当前节点的所有子元素。
# descendant	                    选取当前节点的所有后代元素（子、孙等）。
# descendant-or-self	            选取当前节点的所有后代元素（子、孙等）以及当前节点本身。
# following	                        选取文档中当前节点的结束标签之后的所有节点。
# namespace	                        选取当前节点的所有命名空间节点。
# parent	                        选取当前节点的父节点。
# preceding	                        选取文档中当前节点的开始标签之前的所有节点。
# preceding-sibling	                选取当前节点之前的所有同级节点。
# self	                            选取当前节点。
result19 = html.xpath('//li[1]/ancestor::*') # 选取第一个li节点的所有祖先节点
