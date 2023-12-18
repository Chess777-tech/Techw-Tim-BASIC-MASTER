def f1(x):
    return x + x/2

nums = [1,5,6,7,2]

newlist = list(map(f1,nums))

print(newlist)

# This will create a new list where each element at index i is f1(nums[i])