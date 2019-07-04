import numpy as np 
import time
import sys
import functools

# SIZE = 1000
# l1 = range(SIZE)
# l2 = range(SIZE)

# a1 = np.arange(SIZE)
# a2 = np.arange(SIZE) 
# #python list
# start = time.time()
# result = [(x+y) for x,y in zip[l1,l2]]
# print('python list took ',(time.time()-start)*1000)
# #numpy array
# start = time.time()
# result = a1+a2
# print('My numpy took ',(time.time()-start)*1000)

a = np.array([[1,2],[3,4,],[5,6]],dtype='float64')
print(a.shape)