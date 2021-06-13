str = input("Enter a word: ")

newWord = reversed(str)
#if str == str[::-1]: or
if list(str) == list(newWord):
    print("Palindrome")
else:
    print("not Palindrome")