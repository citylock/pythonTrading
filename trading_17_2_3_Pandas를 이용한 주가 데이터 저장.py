import pandas as pd
import pandas_datareader.data as web
import datetime
import sqlite3

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2017, 7, 1)

gs = web.DataReader('KRX:078930', 'google', start, end)


con = sqlite3.connect("E:\workspace\pycharm\pythonTrading\db\kospi.db")

gs.to_sql('078930', con, if_exists='replace')

read_gs = pd.read_sql("select * from '078930'", con, index_col='Date')

con.close()