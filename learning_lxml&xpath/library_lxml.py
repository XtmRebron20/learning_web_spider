'''
学习链接：https://www.jianshu.com/p/e084c2b2b66d
         https://www.lagou.com/lgeduarticle/82328.html
lxml大部分功能都存在lxml.etree模块中，使用时应from lxml import etree
该模块主要功能是将字符串或流解析成ElemenTree，或者将ElemenTree转换为字符串或流
方法包括：
etree.fromstring(string) ，将字符串解析为Elent或ElementTree
etree.parse(file) ，将文件或者是file_like对象解析为ElementTree（并不是Element，因为parse()一般解析整篇文档），只能对标准的文档使用。
之所以使用etree.parse()方法解析 html 内容时，会报lxml.etree.XMLSyntaxError的错，是因为etree.parse()默认使用的是XML的解析器，
所以当html内容不规范，比如出现某个标签缺少闭合标签时，就会报这个错误。这时，可使用etree.HTMLParser()创建一个HTML的解析器，然后作为etree.parse()方法的参数即可。
etree.XML/HTML 行为类似fromstring，可以对不标准XMl或HTML解析并补全内容
etree.tostring(element) ，将一个 Element 或者 ElementTree 转换为 string 形式。
'''
from lxml import etree
xml_string = '''
    <body>
        <div>
            <ul>
                <li>01</li>
                <li>02</li>
                <li>03</li>
                <li>04</li>
                <li>05</li>
                <li>06</li>
                <li>07
            </ul>
        </div>
    </body>
    ''' # 这段html中07后缺少一个</li>
xml = etree.HTML(xml_string)
result = etree.tostring(xml)
print(result.decode('utf-8')) # 自动补全了<html><body>两个标签，补上了缺失的</li>。可以将不标准的HTML转化为标准的HTML文档


#或者使用parse()方法直接解析文件
# html = etree.parse('./learning_xpath&lxml/test.html', etree.HTMLParser())
# reuslt2 = etree.tostring(html) # 转化为字符串是二进制bytes类型，需要解码打印
# print(reuslt2.decode('utf-8'))