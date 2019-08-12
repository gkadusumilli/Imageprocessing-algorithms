import cv2
import numpy as np


#load the image
img1=cv2.imread("g.jpeg")
img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)


#log transformation formula
img_log=(np.log(img+1)/(np.log(1+np.max(img))))*255

#specify datatype
img_log=np.array(img_log,dtype=np.uint8)

#display the image
cv2.imshow('log image',img_log)
cv2.imshow('original',img)
