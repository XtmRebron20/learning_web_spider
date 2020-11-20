'''
通常情况下json数据以字符串形式存储
使用json库中的loads()转换为供python使用的数据形式
使用dumps()将pyhton的数据格式转换为json格式
'''
# json字符串中的键名和键值需要用双引号包围，单引号会报错
# 而且在最后一个值后面不能加逗号！！！！！
import json
json_str = '''
[
    {
        "name":"xby",
        "age":"24"
        },
    {
        "name":"zxc",
        "age":"12"
        }
]
'''
python_data = json.loads(json_str)
print(python_data)
# 打开外部文件
with open("./learning_save_data/data.json", "r",) as f:
    str = f.read()
    data = json.loads(str)
    print(data)

# 使用dumps()转化为json格式并保存在本地
with open("./learning_save_data/data2.json", "w") as f:
    f.write(json.dumps(data, indent=2))
# indent 参数可以设置自动缩进的空格数量

# dumps() 中的 ensure_ascii=False 参数可以使中文正常保存，并且open()参数中设置为 encoding="utf-8"
data2 = [
    {
        "name":"小明",
        "age":"21"
        }
]
with open("./learning_save_data/data3.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(data2, indent=2, ensure_ascii=False))
