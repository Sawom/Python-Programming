import re
pattern = r"color"
if re.match(pattern,"red is color, blue is also a color") :
    print("match")
else:
    print("not match")