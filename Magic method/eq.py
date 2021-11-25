#get called on comparison using == operator
class marks:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __eq__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2

        if r1 == r2:
            return True
        else:
            return False

s1 = marks(80,65)
s2 = marks(55,90)

if s1 == s2:
    print(" both are equal!")
else:
    print(" not equal! ")