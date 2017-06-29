import numpy as np


# cast list to numpy array

my_list = [1,2,3,4]
print (my_list)

arr = np.array(my_list)
print(arr)


# example 2 : list of list

my_mat = [ [1,2,3], [4,5,6], [7,8,9]]
print(my_mat)

my_arr_mat = np.array(my_mat)
print(my_arr_mat)

# example 3 :

# start, stop
print (np.arange(0, 10))

# start, stop, step-size
print (np.arange(0, 11, 2))

# numpy function : zero
print (np.zeros(5))
print (np.zeros((2,3)))


# numpy function : ones
print (np.ones(5))
print (np.ones((2,3)))

# numpy function : linspace
# start, stop, number of points
print (np.linspace(0, 5, 10))



# random number
# uniform random distribution - 0 ~ 1
print (np.random.rand(5))

# standard normal distribution
print (np.random.randn(5))
print (np.random.randn(4,4))

# random integer number
# 1 - inclusive, 100 - exclusive
print (np.random.randint(1, 100))
print (np.random.randint(1, 100, 10))

# array reshape
arr = np.arange(25)
print (arr)
arr_reshape = arr.reshape((5,5))
print (arr_reshape)


# array MAX and MIN function
ranarr = np.random.randint(0, 50, 10)
print (ranarr)
print (ranarr.max())
print ('Index of max: ' + str(ranarr.argmax()))
print (ranarr.min())
print ('Index of min: ' + str(ranarr.argmin()))


# array attributes
print (arr.shape)       # array shape
print (arr.dtype)       # array datatype for elements


