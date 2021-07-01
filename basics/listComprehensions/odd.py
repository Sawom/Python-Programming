list1 = input("input numbers:")
list2 = list(map(int,list1.split()))
print(list2)
odd = [x for x in list2 if x%2!=0]
print(odd)