import requests
url = "http://dimikcomputing.com"
response = requests.get(url)
with open('dimik.html','w',encoding=response.encoding) as f:
    f.write(response.text)