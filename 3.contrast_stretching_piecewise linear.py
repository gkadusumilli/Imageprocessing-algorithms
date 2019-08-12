import cv2
import numpy as np

#read the image
img=cv2.imread('gray.png',0)



#create zeros array to store the stretched image
minmax_img=np.zeros((img.shape[0],img.shape[1]),dtype='uint8')

#loop over the image and apply min-max formula
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        minmax_img[i,j]=255*(img[i,j]-np.min(img))/(np.max(img)-np.min(img))

#display stretched image
cv2.imshow('Minmax',minmax_img)
