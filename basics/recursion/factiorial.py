num = int(input("Enter a number: "))

def factorial(num):
    if num == 0:
        return None
    if num == 1:
        return 1
    else:
        return num*factorial(num-1)

result = factorial(num)
print("factiorial of",num,"=",result)