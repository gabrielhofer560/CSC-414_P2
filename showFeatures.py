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

img = cv2.imread('j.png',0)


def showFeatures(img,feat):
    for i in feat:
        img[i[0],i[1],:]=[255,0,0]

    #io.imshow((img * 255).astype(np.uint8)  , vmin=0, vmax=255, cmap="gray")
    io.imshow(img,vmin=0,vmax=255)
    io.show()
    

