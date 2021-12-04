import pymysql
con = pymysql.connect(db="db_petugas", user="root", passwd="",host="localhost",port=3306,autocommit=True)
cur = con.cursor()
cur.execute("SELECT * FROM petugas")
data = cur.fetchall()
print(data)
