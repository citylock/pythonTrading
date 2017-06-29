import numpy as np
import pandas as pd

label = ['a', 'b', 'c', 'd']
my_data = [10, 20, 30, 40]
arr = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

print (label)
print (my_data)
print (arr)
print (d)

# pandas Series
print (pd.Series(data=my_data))
print (pd.Series(data=my_data, index=label))
print (pd.Series(my_data, label))
print (pd.Series(arr, label))



ser1 = pd.Series([1,2,3,4], ['USA', 'Germany', 'USSR', 'Japan'])
print (ser1)
ser2 = pd.Series([1,2,5,4], ['USA', 'Germany', 'Italy', 'Japan'])
print (ser2)