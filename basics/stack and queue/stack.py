book = []
print("enter books: ")
for i in range(4):
    book.append(input())

print(book)
book.pop()
print(book)
book.pop()
print(book)
book.pop()
print(book)

if not book:
    print("no book is here")