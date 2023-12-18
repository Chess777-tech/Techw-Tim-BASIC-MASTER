def isAone(x):
    return x == 1

nums = [1,1,6,7,8,1,1,1]

new_list = list(filter(isAone,nums))
print(new_list)
# new_list = [1,1,1,1,1]
