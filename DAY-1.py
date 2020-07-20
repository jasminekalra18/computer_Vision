# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 01:29:15 2020

@author: HP
"""
import cv2
import numpy as np
#CAPTURING VIDEO
video=cv2.VideoCapture(0)

while(True):
    ret,frame=video.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Scale Feed",grey)
    cv2.waitKey(1)
    if cv2.waitKey(33)==27:
        break
cv2.destroyAllWindows()
video.release()
#DRAWING SHAPES
import cv2
import numpy as np
img=np.zeros((400,400,3),dtype="uint8")
img[:,:]=[255,255,255]
a=img.copy()
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
(x, y) = (int(img.shape[1]/2), int(img.shape[0]/2))
d=img.copy()
line=cv2.line(d,(50,50),(350,350),(0,0,255),3)
line2=cv2.line(d,(50,350),(350,50),(0,0,255),3)
rectangle_1 = cv2.rectangle(d,(50, 50), (350, 350), (0, 0, 255), 3)
circle_ = cv2.circle(d, (x,y), (60), (0, 0, 255), 3)
circle_1 = cv2.circle(d, (x,y), (120), (0, 0, 255), 3)
cv2.imshow('combiined', d)
cv2.waitKey(0)
cv2.destroyAllWindows()
img2=np.zeros((500,500,3),dtype='uint8')
center_point=(int(img2.shape[0]/2),int(img2.shape[1]/2))

ellipse=cv2.ellipse(img2,center_point,(100,150),0,0,360,(120,23,45),4)

pts = np.array([[25, 70], [25, 160],  
                [110, 200], [200, 160],  
                [200, 70], [110, 20]], 
               np.int32)
ploygon=cv2.polylines(img2,[pts],True,(43,78,127),6)
cv2.imshow("Ploygon and Ellipse",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

