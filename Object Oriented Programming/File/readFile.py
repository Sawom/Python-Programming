file = open("demo.txt","r+")
text = file.read()
print("is this file readable??  ",file.readable())
print()
print(text)

print("size of file = ",len(text))

'''
print("printing file by lopp... ")
for line in file:
    print(line)
'''
file.close()
