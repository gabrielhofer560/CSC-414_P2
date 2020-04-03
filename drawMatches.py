"""
draw lines showing feature matches
"""
import cv2
import math
import numpy as np
from showKeypoints import showKeypoints
from skimage import io

"""
Description - draws a blue line
source: https://en.wikipedia.org/wiki/Digital_differential_analyzer_(graphics_algorithm)
:param img - image
:param one - (x0,y0)
:param two - (x1,y1)
:param c - color
"""
def line1(img,one,two,c):
    x0,y0=one
    x1,y1=two
    if y0==y1: return
    dx=x1-x0
    dy=y1-y0
    step=max(abs(dx),abs(dy))
    dx/=step
    dy/=step
    x=x0
    y=y0
    i=0
    while i<step:
        img[int(x),int(y)]=c
        x+=dx
        y+=dy
        i+=1

"""
Description - draws lines between matching descriptors
:param img0 - image 1
:param kp0 - keypoints 1
:param img1 - image 2
:param kp1 - keypoints 2
:param matches - matches keypoints 
"""
def drawMatches(img0,kp0,img1,kp1,matches):
    img2 = np.zeros((
        max(img0.shape[0],img1.shape[0]),
        img0.shape[1]+img1.shape[1],
        3),np.uint(8))
    img2[0:img0.shape[0],0:img0.shape[1]] = img0
    img2[0:img1.shape[0],img0.shape[1]:img0.shape[1]+img1.shape[1]] = img1
    nkp1=[] # translate coordinate of right image
    for i in range(len(kp1)):
        nkp1.append([kp1[i][0],img0.shape[1]+kp1[i][1]])
    for [i,j] in matches:
        one,two = kp1[i], nkp1[j]
        line1(img2,one,two,[0,0,255])
    return img2



