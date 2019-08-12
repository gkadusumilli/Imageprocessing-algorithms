# import Opencv 
import cv2 
  
# import Numpy 
import numpy as np 
  
# read a image using imread 
img = cv2.imread('gray.png', 0) 
  
# creating a Histograms Equalization 
# of a image using cv2.equalizeHist() 
equ = cv2.equalizeHist(img) 
  

  
# show image input vs output 
cv2.imshow('image',equ)
cv2.imshow('original',img)
  
cv2.waitKey(0) 
cv2.destroyAllWindows()
