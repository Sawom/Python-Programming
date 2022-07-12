# Python program to demonstrate
# multilevel inheritance

# Base class
class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername


# Intermediate class
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        # invoking constructor of Grandfather class
        super().__init__(grandfathername)
        self.fathername = fathername


# Derived class
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        # invoking constructor of Father class
        super().__init__(fathername, grandfathername)
        self.sonname = sonname

    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)


#  Driver code
s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()