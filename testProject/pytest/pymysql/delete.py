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


# 定义将要执行的SQL语句
sql = "delete from loginin where usr=%s;"
# 拼接并执行SQL语句
cursor.execute(sql, ['june'])

# 涉及写操作要注意提交
conn.commit()

cursor.close()
conn.close()