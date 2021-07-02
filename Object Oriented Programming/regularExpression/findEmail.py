import  re
text = 'email your feedback here : book@subeen.com book@suben sawom124@gmail.com thank you'
result = re.findall(r'(\w+@\w+\.\w+)',text)
print(result)
