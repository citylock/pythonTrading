import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5, 4), ['a', 'b', 'c', 'd', 'e'], ['x', 'y', 'w', 'z'])

# conditional selection along with DataFrame
booldf = df > 0

print (df[booldf])

print (df[df>0])



# 한컬럼에 대한 조건을 가지고 보여주고 싶다면.
print (df[df['w']>0])


# 예 'z' 컬럼이 0보다 작은 row 만 출력
print (df[df['z'] < 0 ])

# multiple condition
print (df[(df['w'] > 0) & (df['z'] > 1)])
