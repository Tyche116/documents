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

# 执行sql语句
 
sql='select * from loginin where usr = %s and pwd = %s'
print("sql:",sql)
res=cursor.execute(sql, ['root', '123456'])
print("res:",res)
print("data:",cursor.fetchall())
 
cursor.close()
conn.close()
 
# 进行判断
if res:
    print('登录成功')
else:
    print('登录失败')