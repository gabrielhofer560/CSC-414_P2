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

def showFeatures(img,loc,D):
    for i in loc:
        for j in range(-7,8):
            img[i[0]+j,i[1]+8,:]=[255,0,0]
            img[i[0]+j,i[1]-7,:]=[255,0,0]
            img[i[0]+8,i[1]+j,:]=[255,0,0]
            img[i[0]-7,i[1]+j,:]=[255,0,0]

#io.imshow((img * 255).astype(np.uint8)  , vmin=0, vmax=255, cmap="gray")
    io.imshow(img,vmin=0,vmax=255)
    io.show()
    
