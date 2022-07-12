class A:
    def func(self):
        print("from class A")

class B(A):
    def func(self):
        print("from class B")
        super().func()

class C(A):
    def func(self):
        print("from class C")
        super().func()

class D(B,C):
    def func(self):
        print("from class D")
        super().func()

print(D.mro())
print(D.__mro__)