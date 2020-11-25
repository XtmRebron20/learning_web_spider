'''
表的创建
'''
import pymysql

# 需要注意，当创建完库后，还需要加入一个db参数指明库的名字
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()
# 通常在外部定义sql语句，然后当做参数传入
sql = '''
CREATE TABLE IF NOT EXISTS students 
(
    id VARCHAR(255) NOT NULL, 
    name VARCHAR(255) NOT NULL, 
    age INT NOT NULL, 
    PRIMARY KEY(id)
    )
'''
cursor.execute(sql)
db.close
