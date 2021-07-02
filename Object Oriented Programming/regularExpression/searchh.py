import re
pattern = r"blue"
if re.search(pattern,"sky is blue, my underware is also blue , xd"):
    print("match")
else:
    print("not matched")