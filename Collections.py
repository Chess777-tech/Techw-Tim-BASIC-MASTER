import collections
from collections import Counter

c = Counter("hello")
print(c)

# This will print Counter({'h':1, 'e':1, 'l':2, 'o':1})


c = Counter([1,1,1,3,4,5,6,7, 7])

c.most_common(1)  # returns [(1, 3)]
c.most_common(2)  # returns [(1, 3), (7, 2)]



