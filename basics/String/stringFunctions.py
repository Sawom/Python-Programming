'''
name = input("Enter your name : ")
print(name)
length = len(name)
print("total character = ",length)

for i in name:
    print(i)

c= ['A','B','c']
c[0]= 'a'
print(c)
# add string
country = "Bangla" + "desh"
print(country)
for i in country:
    print(i)
# string search
print("index 1 =",country.find("Bang"))
print("index 2 =",country.find("la"))
print("index 3 =",country.find("desh"))
print("index 4 =",country.find("BAng"))
'''
#replace
text = "abdur rashid sawom"
ntext = text.replace('abdur','Abdur')
ntext = text.replace('rashid','Rashid')
print("new text = ",ntext)
# strip
text = "     abdur rashid sawom    "
newtext = text.strip()
print("after strip = ",newtext)
# upper & lower
uptext = text.upper()
print("after upper text = ",uptext)
lowText = uptext.lower()
print("after lower text  = ",lowText)
#split
sp = text.split()
print("after split = ",sp)
print("count = ",text.count("abdur"))
# startswith & endswith
new = "mr python pro"
print(" start with = ",new.startswith('mr'))
print(" start with = ",new.endswith('fggr'))

if new.startswith("mr"):
    print("Dear Sir "+ new)



