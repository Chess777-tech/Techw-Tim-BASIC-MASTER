class Vechile():
    def __init__(self,price,color):
        self.price = price 
        self.color = color 
        self.gas = 0 
    
    def fillUpTank(self):
        self.gas = 100 
    
    def emptyTank(self):
        self.gas = 0
    
    def gasLeft(self):
        return self.gas

class Truck(Vechile):
    def __init__(self,price,color,tires):
        super().__init__(price,color)
        self.tires = tires
    
    def beep(self):
        print("Honk Honk")

class Car(Vechile):
    def __init__(self,price,color,speed):
        super().__init__(price,color)
        self.speed = speed 
    
    def beep(self):
        print("Beep Beep")


#Instantiate objects 
truck = Truck(price=30000, color = "Red", tires = 6)
car = Car(price=20000,color = "Blue",speed=120)

#Acessing methods and attributes 
truck.fillUpTank()
car.emptyTank()

#Printing gas left 
print("Gas left in the truck:", truck.gasLeft())
print("Gas left in the car:", car.gasLeft())

#Using beep method
truck.beep()
car.beep()

