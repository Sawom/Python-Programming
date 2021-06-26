class rectangle:
    def area(self):
        area = dim1 * dim2
        print("area of rectangle = ", area)

class triangle:
    def area(self):
        area = 0.5 * dim1 * dim2
        print("area of triangle = ", area)

class square:
    def area(self):
        area = dim5 * dim5
        print("area of square = ", area)

print("For Rectangle: ")
dim1 = int(input("Enter Height: "))
dim2 = int(input("Enter width: "))
r = rectangle()
r.area()
print()
print("For Triangle: ")
dim3 = int(input("Enter Height: "))
dim4 = int(input("Enter base: "))
t = triangle()
t.area()

print("For square: ")
dim5 = int(input("Enter Height: "))
s = square()
s.area()
