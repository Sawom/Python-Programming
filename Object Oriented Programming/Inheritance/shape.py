class shape:
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        print("From area...")

class rectangle(shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("area of rectangle = ",area)

class triangle(shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("area of triangle = ", area)

print("For Rectangle: ")
dim1 = int(input("Enter Height: "))
dim2 = int(input("Enter width: "))
r = rectangle(dim1,dim2)
r.area()

print()

print("For Triangle: ")
dim3 = int(input("Enter Height: "))
dim4 = int(input("Enter base: "))
t = triangle(dim3,dim4)
t.area()