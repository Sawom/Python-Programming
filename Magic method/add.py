class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        r1 = self.m1 + other.m1
        r2 = self.m2 + other.m2
        r3 = student(r1,r2)
        return r3

marks1 = student(69,96)
marks2 = student(60,99)
marks3 = marks1 + marks2

print("m1 = ",marks3.m1)
print("m2 = ",marks3.m2)