list1 = input("Enter some numbers: ")
list2 = list1.split()

def summ(list2):
    sum = 0
    for i in list2:
        sum = sum+int(i)
    return sum

sresult = summ(list2)
avg = summ(list2)/len(list2)

print("sum = ",sresult)
print("average = ",avg)