'''
直接使用DELETE语句
'''
import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()

table = 'students'
condition = 'age > 20'

sql = '''
DELETE FROM {table}
WHERE {condition}
'''.format(table=table, condition=condition)

try:
    if cursor.execute(sql):
        print('true')
        db.commit()
except:
    print('error')
    db.rollback()
db.close()