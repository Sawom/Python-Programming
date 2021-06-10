num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

def add(num1,num2):
    sum = num1+num2
    print("addition = ",sum)

def sub(num1,num2):
    subs = num1-num2
    return subs
result = sub(num1,num2)

def mul(num1,num2):
    muls = num1*num2
    return muls
mresult = mul(num1,num2)

def div(num1,num2):
    divs = num1/num2
    print("division = ",divs)

add(num1,num2)
print("substruction = ",result)
print("multiplication = ",mresult)
div(num1,num2)