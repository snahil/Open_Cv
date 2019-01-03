import numpy
import cv2
import requests as np

# install "IP WEBCAM" go get the ip 


url = "http://123.5668.325:8080/shot.png"


#url connect
geturl = requests.get(url)

#url photo python load
photoweb = geturl.content

#photo binary (bytes) into byte array
photobyte = bytearray(photoweb)


#bytearray convert into ID array

imageid = np.array(photobyte)

#image show

cv2.imshow('welcome', frame)
cv3.waitkey()
cv2.destroyAllwindows()

