"""
description: displays a red square depicting the dominant orientation.
param loc: [x,y] - location
param scale: scale that the feature was detected at
param orient: dominant orientation
return: returns nothing. overlays feature locations on top of the image
"""
from skimage import io
import cv2
import numpy as np
import math

def showFeatures(img,loc,D):
    print("lenth of loc and D: "+str(len(loc))+" , "+str(len(D)))


    for p in range(min(len(loc),len(D))):
        r,c=loc[p]
        dr=D[p][0]
        if D[p][0]%2==0:
            #something
            for j in range(11):
                img[r-j,c-11+j]=[255,0,0]
                img[r+j,c+11-j]=[255,0,0]
                img[r-11+j,c+j]=[255,0,0]
                img[r+11-j,c-j]=[255,0,0]
        else:
            #something else
            for j in range(-7,8):
                img[r+j,c+8,:]=[255,0,0]
                img[r+j,c-7,:]=[255,0,0]
                img[r+8,c+j,:]=[255,0,0]
                img[r-7,c+j,:]=[255,0,0]

        if dr==0:
            for j in range(7):
               img[r+j,c+j]=[255,0,0]
        if dr==1:
            for j in range(7):
               img[r-j,c+j]=[255,0,0]
        if dr==2:
            for j in range(7):
               img[r+j,c+j]=[255,0,0]
        if dr==3:
            for j in range(7):
                img[r-j,c-j]=[255,0,0]
        if dr==4:
            for j in range(7):
               img[r+j,c-j]=[255,0,0]
        if dr==5:
            for j in range(7):
                img[r+j,c+j]=[255,0,0]
        if dr==6:
            for j in range(7):
               img[r+j,c+j]=[255,0,0]
        if dr==7:
            for j in range(7):
                img[r+j,c+j]=[255,0,0]



#io.imshow((img * 255).astype(np.uint8)  , vmin=0, vmax=255, cmap="gray")
    io.imshow(img,vmin=0,vmax=255)
    io.show()
    
