class A:
    def display(self):
        print("from class A")

class B:
    def display(self):
        print("from class B")

class C(B,A):
    def __init__(self):
        def display(self):
            print("from class C")

class D(C):
    def display(self):
        print("from class D")

ob4 = D()
ob4.display()
ob3 = C()
ob3.display()