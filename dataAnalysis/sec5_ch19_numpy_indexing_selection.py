import  numpy as np


arr = np.arange(0, 11)
print (arr)


# index and slicing
print (arr[8])
print (arr[1:5])

print (arr[:6])
print (arr[5:])

arr[0:5] = 100
print (arr)

arr = np.arange(0, 11)
print (arr)

arr_2d = np.array([[15, 20, 25],[30, 35, 40], [45, 50, 55]])
print (arr_2d)

print (arr_2d[1][2])        # double bracket
print (arr_2d[1,2])         # single bracket
print (arr_2d[:2, 1:])      # sub-section of array


# array filter
arr = np.arange(0, 11)
print (arr)
print (arr > 5)

# array Conditional Selection
bool_arr = arr > 5
print (arr[bool_arr])
print (arr[arr < 3])