class distance:
    def __init__(self,fit=None,inch=None):
        self.fit = fit
        self.inch = inch

    def __add__(self, other):
        fit = self.fit + other.fit
        inch = self.inch + other.inch

        if inch>=12:
            fit = fit + 1
            inch = inch - 12
        dis = distance(fit,inch)
        return dis

    def __str__(self):
        return (f"fit = {self.fit}, inchi = {self.inch}")

d1 = distance(4,10)
d2 = distance(4,7)
d3 = d1 + d2

print("d1 : ",d1)
print("d2 : ",d2)
print("d3 : ",d3)

