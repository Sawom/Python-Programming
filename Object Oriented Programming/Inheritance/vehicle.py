class vehicle:
    """for all class"""
    def __init__(self,name,manufacturer,color,speed):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.speed = speed

    def display(self):
        print("from vechile class")

class motorcycle(vehicle):
    def display(self):
        print("Bike name = ",self.name)
        print("Bike manufacturer = ",self.manufacturer)
        print("Bike color = ",self.color)
        print("Bike speed = ",self.speed)

name = input("Enter bike name: ")
manufacturer = input("Enter bike manufacturer name: ")
color = input("Enter bike color: ")
speed = int(input("Enter bike speed: "))

rover = motorcycle(name,manufacturer,color,speed)
rover.display()