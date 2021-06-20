if __name__ == '__main__':
    num = int(input("enter number: "))

def find_fibonacci(num):
    a=0
    b=1
    c=0
    fiboList = []

    for i in range(1,num+1):
        a=b
        b=c
        c=a+b
        fiboList.append(c)

    return fiboList

if __name__ == '__main__':
    result = find_fibonacci(num)
    print("List of ",num," numbers :")
    print(result)