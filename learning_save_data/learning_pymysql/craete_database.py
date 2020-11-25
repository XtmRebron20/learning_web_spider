'''
连接mysql可以使用第三方库pymysql
import pymysql
此篇总结db的创建方法
'''
import pymysql

# 第一步：使用connect()方法声明一个连接对象
# 需要传入一些参数：host(ip地址), user, password, port
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)
# 第二步：使用cursor()方法获得游标
cursor = db.cursor()
# 第三步：使用execute()方法执行sql语句
cursor.execute('SELECT VERSION()') # 这里执行了一条获得mysql版本号的语句
# 第四步：调用fetchone()方法获得一条数据【？？？】
data = cursor.fetchone()
print('Databass Version:', data)
# 执行一条sql语句，创建一个名为spiders的库,编码为utf-8
# 也可以手动创建，创建的过程只需要进行一次，创建相同名称的库会报错
cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')
# 最后调用close()关闭
db.close()

