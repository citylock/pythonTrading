import sqlite3

con = sqlite3.connect("E:\workspace\pycharm\pythonTrading\db\kospi.db")

cursor = con.cursor()
cursor.execute("SELECT * FROM kakao")

# 한번에 하나의 데이터만 읽어올때 - fetchone
print (cursor.fetchone())


cursor.execute("SELECT * FROM kakao")
# 한번에 모든 데이터를 읽어올때 - fetchall
kakao = cursor.fetchall()

print (kakao)

