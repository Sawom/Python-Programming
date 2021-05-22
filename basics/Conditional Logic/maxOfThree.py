num1 = int(input("enter 1st number: "))
num2 = int(input("enter 2nd number: "))
num3 = int(input("enter 3rd number: "))

if num1 > num2 and num1 > num3:
    print(num1, ' is maximum')
elif num2 > num1 and num2 > num3:
    print(num2, ' is maximum')
else :
    print(num3, " is maximum")