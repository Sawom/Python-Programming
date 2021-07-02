import re
text = "Bangladesh is our country." \
       "Bangla is our language." \
       "python ios a programming language"
s = "bangla english Bangla bangla Bangla2"
print('all = ',re.findall(r'bangla',s))
print("at first = ",re.findall(r'^bangla',s))
print("at last = ",re.findall(r'bangla$',s))
print("ignore case = ",re.findall(r'bangla',s,re.IGNORECASE))

print(re.findall(r'^bangla or bangla$',s))