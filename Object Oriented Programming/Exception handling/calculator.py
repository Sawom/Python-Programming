num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

add = num1+num2
sub = num1-num2
mul = num1*num2

print("addition = ", add)
print("substruction = ", sub)
print("multiplication = ", mul)

try:
    div = num1/num2
    print("division = ",div)

except Exception as e:
    print(e)