#2+4+6+8.....+n

sum = 0
n = int(input("Enter n : "))
for i in range(2,n+1,2):
    print(i)
    sum=sum+i
print("sum of series",sum)