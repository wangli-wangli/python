import pymssql
#连接sql server数据库

conn=pymssql.connect(host="localhost",port=1433,user="sa", password="root",database="world",charset="utf8")
cursor = conn.cursor()
sql = "select * from Product"
cursor.execute(sql)

# 获取总记录数
print(cursor.rowcount)

# 获取一条数据
rs = cursor.fetchone()
print(rs)

# 获取所有数据，返回所有的数据
rs = cursor.fetchall()
print(rs)

cursor.close()
conn.close()