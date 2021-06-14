from random import randint

num = int(input("enter range: "))
print("guess from 0 to  ",num)
guess = int(input())
count = 0
for i in range(10):
    ran = randint(0,guess)
    if guess > num:
        print("Out of range! enter 1 to  ",num)
    else:
        if guess == ran :
            print("correct! +1 ")
            count = count +1
        else:
            print("Wrong number! correct is = ",ran)
    guess = int(input())

print("Total point = ",count)