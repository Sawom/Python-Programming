class A:
    def display(self):
        print("from class A")

class B(A):
    def display(self):
        print("from class B")

class C(B):
    def display(self):
        print("from class C")

class D(C):
    def display(self):
        print("from class D")

print("Running class A")
ob1 = A()
ob1.display()
print()
print("Running class B")
ob2 = B()
ob2.display()
print()
print("Running class C")
ob3 = C()
ob3.display()
print()
print("Running class D")
ob4 = D()
ob4.display()