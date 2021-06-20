num1 = {6,5,6,9,8,5,1,2,3,0}
num2 = set([4,8,9,7,3,2,5,10,11,4,4,5,9,69,10])
print(num2)
num1.add(69)
print(num1)
print(99 in num1)

print("union = ",num1 | num2)
print("intersection = ",num1 & num2)
print("difference = ",num1 - num2)
print("difference2 = ",num2 - num1)
print("uncommon = ",num1 ^ num2)
