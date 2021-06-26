import requests
img1 = "http://goo.gl/PsibBu"
res = requests.get(img1)

with open("pyimg.png",'wb', encoding=res.encoding) as f:
    f.write(res.content)