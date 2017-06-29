import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5, 4), ['a', 'b', 'c', 'd', 'e'], ['x', 'y', 'w', 'z'])

print (df)

# 각각의 column 은 Series 로 구성되어 있다
print (df['w'])

# 멀티 column을 선택할 경우 list 로 선택할수 있다
print (df[['w', 'z']])


# dataframe operation
df['new'] = df['w'] + df['z']
print (df)

# to delete column(axis 1): drop => 실제 데이터가 삭제되는게 아니라 display 에서만 빠지고 df 에는 그대로 있다
# axis 0 -> row , axis 1 -> column
df.drop('new', axis=1)
print (df)


# 실제 데이터를 삭제하기 위해서는 inplace 옵션을 넣어주면 된다
df.drop('new', axis=1, inplace=True)
print (df)


# to delete row(axis 0): drop
df.drop('e')


# Selecting column & row
print (df['w'])             # column

print (df.loc['c'])
print (df.iloc[2])

# sub set of dataframe
print (df.loc[['b', 'c'] ,['x', 'z'] ])



