class Car:
    def __init__(self , brand , model  ):
        self.brand= brand
        self.model= model
        pass
    def move(self):
        print('Drive!')

class Boat: 
    def __init__(self , brand , model):
        self.brand= brand
        self.model = model
        pass
    def move(self):
        print('Sail!')

class Plane:
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model
        pass
    def move(self):
        print('Fly!')

car1 = Car('BMW' , "M65")
boat1 = Boat("Ibiza" , "Touring 20")
plane1 = Plane('Boeing' , 747)

y = (car1 , boat1 , plane1)
        
for x in y:
    x.move()