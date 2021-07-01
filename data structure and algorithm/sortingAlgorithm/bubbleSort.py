list1 = input("input some numbers (for bubble sort) : ")
list2 = list(map(int,list1.split()))
print("elements are = ",list2)
n = len(list2)

for i in range(n):
    for j in range(n-i-1):
        if list2[j] > list2[j+1]:
            temp = list2[j]
            list2[j] = list2[j+1]
            list2[j+1] = temp

print("after sorting elements are = ",list2)