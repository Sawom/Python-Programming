import requests

res = requests.get("http://example.com")
print(res.ok)
print(res.text)

'''res = requests.get("http://facebook.com")
print(res.ok)
print(res.text)'''
