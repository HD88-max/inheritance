# Write a Python program to implement Inheritance by creating a Parent Class Vehicle with a constructor that has details like name, maximum speed, and mileage. Then, create a Child Class Bus that inherits Class Vehicle. Finally, showcase Inheritance to display the details of the Vehicle Bus named - School Volvo.

class Vehicle:

    def __init__(self,name,maxspeed,mileage):
        self.name=name
        self.maxspeed=maxspeed
        self.mileage = mileage

class bus(Vehicle):
    pass

ob = bus("Volvo",100,50)
print("The name of the bus is",ob.name,": the maximum speed is",ob.maxspeed,": the mileage is",ob.mileage)



        