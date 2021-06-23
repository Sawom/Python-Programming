file = open("ex1.txt",'a')
text = input("Enter for input in file: ")
file.write(text)

file = open("ex1.txt",'r')
text1 = file.read()
print(text1)
file.close()