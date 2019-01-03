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

image1d = np.array(photobyte)

#image show

cv2.imshow('welcome', frame)
cv3.waitkey()
cv2.destroyAllwindows()


while True:
    
    geturl = requests.get(url)
    photoweb = geturl.content
    photobyte = bytearray(photoweb)
    image1d = np.array(photobyte)
    frame = cv2.indecode(image1d, -1)
    cv2.imshow('welcome', frame)
    if = cv2.waitkey(1) == 13
        break

    
