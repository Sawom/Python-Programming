#1-2+3-4+5+........
lastNum = int(input("Enter last digit: "))
odd = even = 0

for i in range(1,lastNum+1,1):
    if(i%2==1):
        odd=odd+i
    elif(i%2==0):
        even = even +i

sum = odd-even
print("result = ",sum)