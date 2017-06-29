import numpy as np


arr = np.arange(0, 11)
print (arr)

# array operation
print (arr + arr)
print (arr - arr)
print (arr * arr)

print (arr + 100)
print (arr * 100)


# nan : 0/0, inf : 1/0
print (arr / arr)
print (1 /arr)

#
print (arr ** 2)
print (np.sqrt(arr) )
print (np.exp(arr))
print (np.max(arr))
print (np.sin(arr))