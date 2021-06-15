from collections import deque

bank = deque(['anis','sawom','rashid','bijoy'])
print(bank)
bank.popleft()
print(bank)

bank.popleft()
print(bank)

bank.popleft()
print(bank)

bank.popleft()
print(bank)

if not bank:
    print("no person is here")