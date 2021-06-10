#1^2+2^2+.......+n

num = int(input("enter last digit to print...."))
sum=0
for i in range (1,num+1,1):
    sum=sum+i*i
print("sum = ",sum)