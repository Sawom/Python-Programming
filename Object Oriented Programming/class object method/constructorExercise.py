class car:
    def __init__(self,name,manufacturer,color,year,enginePower):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = year
        self.enginePower = enginePower

    def start():
        print("car has started")

    def brake():
        print("break the car")

    def drive():
        print("drive the car! but do not cross the speed limit!")

    def turn():
        print("turn right...")
        print("then...turn left")

    def changeGear():
        print("change gear and drive safely...good luck")

    def display(self):
        print("car name = ",self.name)
        print("car car manufacturer name = ",self.manufacturer)
        print("car color = ",self.color)
        print("car manufacturer year = ",self.year)
        print("car engine Power = ",self.enginePower)

name = input("Enter car name: ")
manufacturer = input("Enter car manufacturer name: ")
color = input("Enter car color: ")
year = input("Enter car manufacturer year: ")
enginePower = input("Enter engine Power of the car: ")

martin = car(name,manufacturer,color,year,enginePower)

martin.display()
print()
car.start()
car.brake()
car.drive()
car.turn()
car.changeGear()