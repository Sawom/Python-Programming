import  requests
url = "http://facebook.com"

res = requests.get(url)
with open('fb.html','w', encoding = res.encoding) as f:
    f.write(res.text)