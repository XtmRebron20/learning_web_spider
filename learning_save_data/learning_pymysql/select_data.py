'''
使用SELECT FROM语句进行查询
'''
import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()

table = 'students'
condition = 'age >= 20'

sql = '''
SELECT *
FROM {table}
WHERE {condition}
'''.format(table=table, condition=condition)
print(sql)
try:
    cursor.execute(sql)
    print('Count row:', cursor.rowcount) # rowcount属性，获取条目数。
    one = cursor.fetchone() # fetchone()方法，获取指针所指第一条
    print('One:', one)
    results = cursor.fetchall() # fetchall()方法，获取指针当前位置到结束的所有
    # 由于之前调用过fetchon()，所以现在指针处于第二条目上。所以打印时会缺少第一条目
    # 还可以使用循环加fetchone()方法来输出所有条目
    # while row :
    #     print(row)
    #     row = cursor.fetchone()
    print('All:', results)
    print('Type all:', type(results))
    for row in results:
        print(row)


except:
    print('error')
db.close()