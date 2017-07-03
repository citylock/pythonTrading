import pandas as pd
from sqlalchemy import create_engine


# CSV files
df = pd.read_csv("example.csv")
df.to_csv("My_output.csv", index=False)


# Excel files
pd.read_excel("Excel_Sample.xlsx", Sheetname="Sheet1")
df.to_excel("Excel_sample3.xlsx", sheet_name="NewSheet")


# HTML files
data = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')


# SQL
engine = create_engine('sqlite:///:memory:')
df.to_sql('my_table', engine)
sqldf = pd.read_sql('my_table', con=engine)

