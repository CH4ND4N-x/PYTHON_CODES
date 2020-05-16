#download image
import requests
URL='https://wallpaperplay.com/walls/full/d/d/0/98227.jpg'
pic=requests.get(URL)
file = open('local_image.jpg', 'wb')
file.write(pic.content)
file.close
del pic