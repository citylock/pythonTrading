import pandas as pd
from pandas import Series, DataFrame
import sqlite3


con = sqlite3.connect("E:\workspace\pycharm\pythonTrading\db\kospi.db")

# index_col 이 None 이면 자동의 0부터 시작하는 정숫값이 인덱스로 할당된다.
df = pd.read_sql('select * from kakao', con, index_col=None)


# 만일 인덱스 컬럼이 존재하는 경우
df2 = pd.read_sql('select * from kakao', con, index_col='Date')

con.close()

