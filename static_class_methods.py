#static method 

class myClass:
    def __init__(self, x):
        self.x =x 
    
    @staticmethod
    def staticmethod():
        return "I am a static method"

# Notice staticmethod does not requre the self parameter 
    


#class method 

class myClass:
    def __init__(self, x):
        self.x = x 
    
    @classmethod
    def classmethod(cls):
        cls.count += 1
# The classMethod can access and modify class variables. It takes the class name as a required parameter 
