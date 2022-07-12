from abc import ABC,abstractmethod

class shape(ABC):
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2
    @abstractmethod
    def area(self):
        pass

class triangle(shape):
    def area(self,dim1,dim2):
        area = .5*dim1*dim2
        print("area of triangle = ",area)

class rectangle(shape):
    def area(self,dim1,dim2):
        area = dim1*dim2
        print("area of rectangle = ", area)

print("for triangle...")
dim1 = int(input("Enter base: "))
dim2 = int(input("Enter height: "))
t = triangle(dim1,dim2)
t.area(dim1,dim2)
print()
print("for rectangle...")
dim1 = int(input("Enter height: "))
dim2 = int(input("Enter width "))
r = rectangle(dim1,dim2)
r.area(dim1,dim2)
