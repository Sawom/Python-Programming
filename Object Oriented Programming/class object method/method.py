class car:
    brand = ''
    speed = ''
    color = ''

    def set_value(self, brand, speed, color):
        self.brand = brand
        self.speed = speed
        self.color = color

    def display(self):
        print(f"car brand = {self.brand}, car speed = {self.speed}, "
              f"car color = {self.color}")

bmw = car()
print("for car 1")
brand = input("enter brand: ")
speed = input("enter speed: ")
color = input("enter color: ")

bmw.set_value(brand, speed, color)
bmw.display()
print()
print("for car 2")
audi = car()
brand = input("enter brand: ")
speed = input("enter speed: ")
color = input("enter color: ")
audi.set_value(brand, speed, color)
audi.display()
