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
sql = 'select usr,pwd from loginin;'

try:
    cursor.execute(sql)

    # 取到查询结果
    # ret1 = cursor.fetchone()  # 取一条
    # ret2 = cursor.fetchmany(3)  # 取三条
    # ret3 = cursor.fetchone()  # 取一条

    # print(ret1)
    # print(ret2)
    # print(ret3)
    countAll = cursor.fetchall()
    print("data: ",countAll)

except Exception as e:
    print(str(e))
    # 有异常就回滚
    conn.rollback()

 
# 涉及写操作要注意提交
conn.commit()

cursor.close()
conn.close()