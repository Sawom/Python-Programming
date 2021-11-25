# To get called on comparison using >= operator.
class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __ge__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2

        if r1 >= r2:
            return True
        else:
            return False

s1 = student(66,81)
s2 = student(90,59)

if s1>=s2:
    print("s1 win")
else:
    print("s2 win")
