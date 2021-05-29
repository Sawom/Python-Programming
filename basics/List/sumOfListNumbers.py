list1 = input("Enter some numbers: ")
list2 = list1.split()

sum = 0
for i in list2:
    sum = sum + int(i)

print("sum of numbers = ",sum)
