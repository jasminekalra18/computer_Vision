# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 09:17:10 2020

@author: HP
"""

import cv2
import numpy as np
 
rectangle = np.zeros((300, 300), dtype = "uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), (255, 255, 255), -1)
cv2.imshow("",rectangle)
cv2.waitKey(0)
 
 
 
circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, (255, 255, 255), -1)
cv2.imshow("",circle)
cv2.waitKey(0)
 
bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow('',bitwiseNot)
cv2.waitKey(0)

bitwiseXor = cv2.bitwise_xor(circle,rectangle)
cv2.imshow('',bitwiseXor)
cv2.waitKey(0)

cv2.destroyAllWindows()


"""TRANSALTION OPERATION ON THE IMAGE"""

image=cv2.imread("bird.jpg")
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()



(h, w) = image.shape[:2] #Finding Height and Width
(q_h, q_w) =(int(h/4), int(w/4))#Calculating Quarter Height and Quarter Width
m = np.float32([[1, 0, q_w], [0, 1, 0]]) #shift right by quarter of its width


translated = cv2.warpAffine(image, m, (w, h))
cv2.imshow('',translated)
cv2.waitKey(0)

m = np.float32([[1, 0, 0], [0, 1, q_h]]) #shift down by quarter of its height

translated = cv2.warpAffine(image, m, (w, h))
cv2.imshow('',translated)
cv2.waitKey(0)

cv2.destroyAllWindows()
