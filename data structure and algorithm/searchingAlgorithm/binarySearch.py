list1 = input("enter numbers: ")
list2 = list(map(int,list1.split()))
print("Elements are = ",list2)
list2.sort()
print("after sorted,,, elements are = ",list2)
value = int(input("Enter value to search: "))
n = len(list2)

pos = -1
first = 0
last = n-1
mid = (first+last)// 2

while(last>=first):
    if(list2[mid]==value):
        pos=mid
        break
    elif list2[mid] > value:
        last = mid -1
    else:
        first = mid + 1
    mid = (first + last) // 2

if(pos == -1):
    print("sorry not found! ")
else:
    print("found! position = ",pos+1)