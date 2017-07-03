import pandas as pd



# CSV files
df = pd.read_csv("example.csv")

df.to_csv("My_output.csv", index=False)


# Excel files
pd.read_excel("Excel_Sample.xlsx", Sheetname="Sheet1")

df.to_excel("Excel_sample2.xlsx", sheet_name="NewSheet")




