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
sql = "update loginin set pwd=%s where usr=%s;"
# 拼接并执行SQL语句

try:
    cursor.execute(sql, [666666, 'july'])
except Exception as e:
    print(str(e))
    # 有异常就回滚
    conn.rollback()

# 涉及写操作要注意提交
conn.commit()

cursor.close()
conn.close()