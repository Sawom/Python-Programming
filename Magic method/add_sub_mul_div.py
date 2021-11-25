a= 5
b = 10
c = 5
print("add = ",int.__add__(a,b+c))
print("add2 = ",c.__add__(a+b))
print("sub = ",int.__sub__(b+c,a))
print("mul = ",int.__mul__(a,b+c))
print("div = ",int.__truediv__(a+b,c)) #a/b
