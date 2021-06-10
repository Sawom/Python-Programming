list1 = input("Enter some numbers")
list2 = list1.split()

def add(list2):
    sum = 0
    for i in list2:
        sum = sum +int(i)
    print(sum)

add(list2)