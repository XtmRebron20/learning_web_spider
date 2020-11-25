'''
数据的插入方法
'''
import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()

# id = '20120001'
# age = '22'
# user = 'Bob'

# sql = '''
# INSERT INTO students(id, name, age)
# VALUES(%s, %s, %s)
# '''
# # try except 语句是标准的数据修改格式
# # 该结构可以称之为一个事物，
# # 事物机制可以保证数据的：一致性
# # 即一组事务，要么全部成功，要么全部失败
# # 请务必使用它
# try:
#     cursor.execute(sql, (id, user, age))
#     print('true')
#     db.commit() # 数据的插入，更新，删除操作之后，都需要调用commit()方法进行提交
# except:
#     print('false')
#     db.rollback() # 若发生错误，则进行回滚。相当于什么都没发生
# db.close

# 通常数据都是通过一个动态字典传入的
data = {
    'id':'20120003',
    'name':'xby',
    'age':'24'
}
table = 'students'
keys = ','.join(data.keys()) # 键名用逗号连接
values = ','.join(['%s'] * len(data)) # 只是构建了多个%s占位符，还未开始传值
sql = '''
    INSERT INTO {table}({keys})
    VALUES ({values})
'''.format(table=table, keys=keys, values=values)
try:
    if cursor.execute(sql, (tuple(data.values()))): # 开始传键值,一定要使用【元组】！！！
        print('Successful')
        db.commit()
except:
    print('Error')
    db.rollback()
db.close()

# 通常报错的原因是sql语句写错，仔细检查
# 主键的值唯一，不可添加重复主键



