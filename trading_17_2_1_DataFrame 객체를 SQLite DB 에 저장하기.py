import pandas as pd
from pandas import Series, DataFrame
import sqlite3

raw_data = {'col0': [1, 2, 3, 4], 'col1': [10, 20, 30, 40], 'col2':[100, 200, 300, 400]}

df = DataFrame(raw_data)


con = sqlite3.connect("E:\workspace\pycharm\pythonTrading\db\kospi.db")

df.to_sql('test', con)

