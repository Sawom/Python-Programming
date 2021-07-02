import re
pattern = r"red"
text = "blood is red , but not feelings are red,,  whatever, xd"
match = re.search(pattern,text)

if match:
    print(match.start())
    print(match.end())
    print(match.span())