list1 = input("enter some numbers: ")
list2 = list(map(int,list1.split()))
print(list2)
result = [x for x in list2 if x %2==0]
print("even numbers are: ")
print(result)