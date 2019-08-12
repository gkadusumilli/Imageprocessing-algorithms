import numpy as np
import cv2
img=cv2.imread("g.jpeg")
gamma_two_point_two=np.array(255*(img/255)**2.2,dtype='uint8')
gamma_point_four=np.array(255*(img/255)**0.4,dtype='uint8')

cv2.imshow('a2',gamma_two_point_two)
cv2.imshow('a3',gamma_point_four)

