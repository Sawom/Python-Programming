#1+2+3+4........n
num = int(input("enter n..."))
sum = 0
'''
for i in range(num+1):
    if i%2==1 :
        print(i)
        sum=sum+i
'''
#or
for i in range(1,num+1,2):
    print(i)
    sum=sum+i

print("sum of series= ",sum)