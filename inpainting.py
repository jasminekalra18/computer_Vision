# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 02:41:34 2020

@author: HP
"""
import cv2

img = cv2.imread(r'C:\Users\HP\Desktop\sample.jpg') 
cv2.imshow("",img)
mask = cv2.imread(r'C:\Users\HP\Desktop\sample2.jpg', 0) 
cv2.imshow("",mask)
# Performing Inpainting
ns = cv2.inpaint(img, mask, 1, cv2.INPAINT_NS) 
telea = cv2.inpaint(img, mask, 1, cv2.INPAINT_TELEA)
# Displaying Results
cv2.imshow("",ns)
cv2.imshow("",telea)
cv2.waitKey(0)
cv2.cv2destroyAllWindows()

