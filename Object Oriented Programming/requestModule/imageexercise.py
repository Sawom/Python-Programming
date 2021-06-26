import  requests
imgg = "http://pcwalls.net/wp-content/uploads/2014/09/Happy-girl-wallpaper.jpg"
r = requests.get(imgg)
with open("immgg.png",'wb', encoding=r.encoding) as f:
    f.write(r.content)
