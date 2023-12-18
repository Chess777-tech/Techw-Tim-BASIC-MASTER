import numpy as np


arr = np.zeros((2,3))
print(arr) 


arr = np.ones((2,3))
print(arr)


arr = np.arange(10)
print(arr) # 0-9


arr = np.arange(4,10,2)
print(arr)


arr = np.arange(0,1,0.1)
print(arr)



arr = np.linspace(1,3,6)
print(arr)\
# The linespace function will automatically calculate the step value 
# based on the number of elements we specify 


arr = np.eye(3)
print(arr) # ->       ([[1., 0., 0.],
#                      [0., 1., 0.],
#                      [0., 0., 1.]]


arr = np.random.random((2,2))
print(arr)


arr = np.ones((3,3), dtype = int)

arr = np.zeros((2,2), dtype = str )