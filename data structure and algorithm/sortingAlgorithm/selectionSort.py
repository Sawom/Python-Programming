list1 = input("input some numbers (for selection sort) : ")
list2 = list(map(int,list1.split()))
print("elements are = ",list2)
n = len(list2)

for i in range(n):
    for j in range(n):
        if list2[i] < list2[j] :
            temp = list2[i]
            list2[i] = list2[j]
            list2[j] = temp

print("after sorted elements are: ",list2)