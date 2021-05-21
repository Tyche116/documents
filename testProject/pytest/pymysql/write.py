# 导入pymysql模块
import pymysql
 
# 连接database
conn = pymysql.connect(
    host='127.0.0.1',
    port=3600,
    user='root',password='123456',
    database='test2',
    charset='utf8')
 
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()  


# 定义要执行的sql语句
sql = 'insert into loginin(usr,pwd) values(%s,%s);'
data = [
    ('july', '147'),
    ('june', '258'),
    ('marin', '369')
]
# 拼接并执行sql语句
cursor.executemany(sql, data)


sql2 ='insert into loginin (usr,pwd) values (%s,%s);'
cursor.execute(sql2, ['wuli', '123456789'])
 
# 涉及写操作要注意提交
conn.commit()

cursor.close()
conn.close()