import cv2
import numpy as np

#load the original image
img=cv2.imread('g.jpeg')
images=[]
for _ in range(20):
    img1=img.copy()
    cv2.randn(img1,(0,0,0),(50,50,50))
    images.append(img+img1)
#for averaging create an empty array then add images to this array
    img_avg=np.zeros((img.shape[0],img.shape[1],img.shape[2]),np.float32)
    for im in images:
        img_avg=img_avg+im/20
#roundoff the float values,always specify the dtype
        img_avg=np.array(np.round(img_avg),dtype=np.uint8)

#display the iamges
    cv2.imshow('average_img',img_avg)
    cv2.imshow('original_img',img)
    cv2.imshow('noisy_images',images[1])
    cv2.waitKey(0)
