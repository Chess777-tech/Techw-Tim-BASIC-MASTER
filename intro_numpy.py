import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
print(arr[1,1]) # -> 5 
# use this to index

arr = np.array([[1,2,3],[4,5,6]])
print(arr.siz) # -> 6


arr = np.array([[1,2,3],[4,5,6]])
print(arr.ndim) # -> 2
# use this to see the amount of dimension


arr = np.array([1,2,3])
arr = np.append(arr, 7)

print(arr) # ->([1,2,3,7])
# use this to add things into our array

arr = np.array([1,2,3])
arr = np.delete(arr, 0)

print(arr)
# to delete something we use np.delete(array,index)