import re
st = "bangladesh"
match = re.search(".",st)
print(match.group())

match = re.search("b.n.....s.",st)
print(match.group())




