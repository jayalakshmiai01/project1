import mysql.connector
con=mysql.connector.connect(
    host="192.168.1.240",
    user="AIBATCH01",
    password="AI@123",
    database="a"
    )
print(con)
result=con.cursor()
result.execute("show tables")
result_show=result.fetchall()
for x in result_show:
    print(x)
result.execute("select * from sys_info")
result_show=result.fetchall()
for x in result_show:
    print(x)
result.execute("delete from sys_info where sno=4")
result.execute("select * from sys_info")
result_show=result.fetchall()
for x in result_show:
    print(x)
