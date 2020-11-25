'''
使用sql语句进行变更数据
'''
import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', db='spiders')
cursor = db.cursor()

# # 一般方法，直接更新
# sql = '''
# UPDATE students
# SET age = %s
# WHERE name = %s
# '''
# try:
#     cursor.execute(sql, (100,'Bob'))
#     print('true')
#     db.commit
# except:
#     db.rollback()
#     print('false')
# db.close()

# 构建动态的动态可更新的sql语句
# 通常在数据爬取的过程中，数据是动态的
# 如果对于新数据就插入，如果是重复数据就更新
data = {
    'id':'20120001',
    'name':'Bob',
    'age':'21'
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data)) 

# ON DUPLICATE KEY  UPDATE
# 如果有相同的主键，则进行数据更新
sql = '''
INSERT INTO {table}({keys})
VALUES ({values})
ON DUPLICATE KEY  UPDATE
'''.format(table=table, keys=keys, values=values)
update = ','.join(['{key} = %s'.format(key=key) for key in data.keys()]) # 为什么会生成三个key=%s?
sql += update
print(sql)

try:
    if cursor.execute(sql, tuple(data.values())*2):
        print('true')
        db.commit()
except:
    print('error')
    db.rollback()
db.close()


