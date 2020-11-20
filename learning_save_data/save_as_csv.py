'''
要使用scv文件需要先导入scv库
import csv
'''
# 写入
import csv

# 每调用一次writerow()方法可以写入一行
# 参数delimiter = ''可以指定每个元素之间间隔用什么隔开，默认逗号
# 也可以同时写入多行，需要用到二维列表
with open('./learning_save_data/data.csv', 'w') as f:
    writer = csv.writer(f) # 初始化一个写入器
    writer.writerow(['id', 'name', 'age']) # 写入行
    writer.writerow(['1000', 'Mike', 20])
    writer.writerow(['1001', 'Bob', 22])
    writer.writerow(['1002', 'xby', 21])

# 一般爬取的数据都会用字典存储
# csv库提供了字典的写入方式
with open('./learning_save_data/data.csv', 'a') as f:
    fildnames = ['id', 'name', 'age'] # 先定义了字段名
    writer = csv.DictWriter(f, fildnames) # 初始化一个写入器
    writer.writeheader() # 将字段明写入文件
    writer.writerow({
        'id':'1000',
        'name':'Mike',
        'age':'20'
    })
    writer.writerow({
        'id':'1001',
        'name':'Bob',
        'age':'22'
    })
    writer.writerow({
        'id':'1002',
        'name':'xby',
        'age':'21'
    })

# 若要写入中文记得open里设置encoding="utf-8"

# 读取
with open('./learning_save_data/data.csv', 'r') as f:
    reader = csv.reader(f) # 创建一个读取器
    for row in reader: # 返回的是一个可迭代对象
        print(row)

# 还可以用pandas中的方法进行读写
import pandas as pd
df = pd.read_csv('./learning_save_data/data.csv')
print(df)
# 写入使用to_csv()方法
