import sqlite3

# 데이터베이스 생서
con = sqlite3.connect("E:\workspace\pycharm\pythonTrading\db\kospi.db")


cursor = con.cursor()

# 테이블 생성
cursor.execute("CREATE TABLE kakao(Date text, Open int, High int, Low int, Closing int, Volumn int)")


# 데이터 생성
cursor.execute("INSERT INTO kakao VALUES('16.06.02', 99000, 99300, 96300, 97500, 556790)")

con.commit()
con.close()

