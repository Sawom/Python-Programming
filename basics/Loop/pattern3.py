'''
3
3 2
3 2 1
'''
num = int(input("enter number: "))

for i in range(num):
    for j in range(i,-1,-1):
        print(j+1,end=" ")
    print()