list1 = input("input some numbers: ")
list2 = list1.split()

def maximum(list2):
    max = list2[0]
    for i in list2:
        if i > max:
            max = i
    return max

def minimum(list2):
    min = list2[0]
    for i in list2:
        if i< min:
            min = i
    return min

mx = maximum(list2)
mn = minimum(list2)

print("maximum number = ",mx)
print("minimum number = ",mn)