list1 = input("input some numbers (for insertion sort) : ")
list2 = list(map(int,list1.split()))
print("elements are = ",list2)
n = len(list2)

for i in range(n):
    temp = list2[i]
    j = i -1
    while j>=0 and list2[j] > temp:
        list2[j+1] = list2[j]
        j= j-1
        list2[j+1] = temp

print("after sorting elements are = ",list2)