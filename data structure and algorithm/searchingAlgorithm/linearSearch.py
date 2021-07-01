list1 = input("enter some numbers: ")
list2 = list(map(int, list1.split()))
x = int(input("Enter value to search: "))
print("elements are = ",list2)

def linear(list2,x):
    n = len(list2)
    i=0
    for i in range(n):
        if list2[i] == x :
            i=i+1
            break

    if i==0:
        print("not found")
    else:
        print("number is found at = ",i)

linear(list2,x)