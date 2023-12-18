import numpy as np
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

x + y  # -> array([[ 6,  8],
#                  [10, 12]])

x - y  # -> array([[-4, -4],
#                  [-4, -4]])

x * y  # -> array([[ 5, 12],
#                  [21, 32]])

x / y  # -> array([[0.2       , 0.33333333],
#                  [0.42857143, 0.5       ]])

np.sqrt(x)  # -> array([[1.        , 1.41421356],
#                       [1.73205081, 2.        ]])

print(x+y)
print(x-y)
print(x*y)
print(x/y)
