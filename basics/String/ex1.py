str = input("Enter a sentence: ")
for st in str:
    if(st >= 'A' and st <= 'Z' ):
        print(st,end='')
print()

for st in str:
    if(st >= 'a' and st <= 'z'):
        print(st,end='')
print()

for st in str:
    if(st >= '1' and st <= '9'):
        print(st,end='')
print()
