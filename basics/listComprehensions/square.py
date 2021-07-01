list1 = input("enter some numbers: ")
list2 = list(map(int,list1.split()))
print(list2)
print(" square in list = ")
square = [x*x for x in list2]
print(square)