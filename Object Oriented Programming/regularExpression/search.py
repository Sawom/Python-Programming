import re
match = re.search('bangla','bangladesh')
print(match)
print(match.group())
match = re.search('desh','bangladesh')
print(match.group())
match = re.search('des','bangladesh')
print(match.group())
match = re.search('dets','bangladesh')
match
print(type(match))