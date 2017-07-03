import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan] , 'B':[5, np.nan, np.nan], 'C':[1,2,3]}

df = pd.DataFrame(d)


# 데이터가 없는 row/col 을  drop 시키는 함수 - axis:0 - row, axis=1 = col
print(df.dropna(axis=1))


print(df.dropna(thresh=2))


# fill in data in na field
print(df.fillna(value='FILLED'))

print(df['A'].fillna(value=df['A'].mean()))