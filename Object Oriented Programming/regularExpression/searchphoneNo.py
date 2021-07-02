import  re
text = "Lorem Ipsum is simply dummy text of the printing and 54 5644 65464 typesetting 017 11101001 industry." \
       " Lorem Ipsum has been the industry's standard 014 58745121 dummy text ever since the 1500s, 01911732266, 01515608007 "

#match = re.findall('\d+',text)
#print(match.group())
print(re.findall('\d{3}\s?\d{8}',text))
print(re.findall('01[56789]\s?\d{8}',text))