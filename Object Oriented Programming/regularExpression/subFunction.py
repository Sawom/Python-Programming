import re
pattern = r'red'
text1 = "blood is red , but feelings are not red,,  whatever, xd"
text2 = re.sub(pattern,'blue',text1)
#text2 = re.sub(pattern,'blue',text1,count=1)
print(text2)