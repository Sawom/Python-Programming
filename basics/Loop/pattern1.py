'''
1
1 2
1 2 3
'''
num = int(input("enter number: "))
for i in range(num):
    for j in range(i+1):
        print(j+1,end=' ')
    print()