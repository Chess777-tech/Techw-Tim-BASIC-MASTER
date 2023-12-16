class Point():
    def __init__(self,x=0,y=0):
        self.x = x 
        self.y = y 
        self.cords = (self.x,self.y)

    def move(self,x,y):
        self.x += x 
        self.y += y
    
    def length(self):
        import math 

        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def __gt__(self,other): # Greater Than 
        return self.length() > other.length()
    
    def __ge__(self,other): # Greater than or Equal to 
        return self.length()>= other.length()

    def __lt__(self,other): # Less than
        return self.length() < other.length()
    
    def __le__(self,other): # Less than or Equal to 
        return self.length() <= other.length()

# We are going to compare points basesd on their lengths 

p1 = Point(3,4)
p2 = Point(3,2)
p3 = Point(1,3) 
p4 = Point(0,1)

isLess = p1 <= p2 #This is false
isGreater = p1 >= p2

print(isLess)
print(isGreater)