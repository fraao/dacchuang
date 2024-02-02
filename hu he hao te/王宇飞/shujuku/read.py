import pymysql

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password= "1234",
    database= "usip",
    charset= "utf8"
)
cur = conn.cursor()
try:
    sql = "select result from t_data"
    cur.execute(sql)
    ret=cur.fetchall()
    ret=list(ret)
    print(ret)
except Exception as e:
    print(e)
    conn.rollback()

cur.close()
conn.close()