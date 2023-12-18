import collections 
from collections import namedtuple

Point = namedtuple("name","paramater 1,parameter 2,paparmeterx")

p = Point(1,4,5)

print(p) # Prints name (parameter1=1, paramater2=4,parameterx=5)





Point = namedtuple("Point","x,y")

p = Point(1,4)

print(p.x) # prints 1
print(p.y) # prints 4
print(p) #prints point (x=1, y=4)