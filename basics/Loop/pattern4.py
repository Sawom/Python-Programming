'''
3
2 3
1 2 3
'''

num = int(input("enter number: "))
for i in range(num):
    for j in range(i,-1,-1):
        print(num-j,end=' ')
    print()