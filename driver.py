"""
Author: Gabriel Hofer
Course: CSC-414
Instructor: Dr. Randy Hoover
"""
from gk import gk
from harris import harris
from showDots import showDots
import numpy as np
import sys
from skimage import io
from skimage.color import rgb2gray

from showFeatures import showFeatures
from sift import printH, makeH, sift

# read image, convert to gray
img = io.imread(sys.argv[1]);
cpy = img
print("orig shape: "+str(img.shape))
gry = rgb2gray(img)
print("gray shape: "+str(gry.shape))

# get list of locations of interest points
loc = harris(gry,gk(3,3,1),0.3)
print("number of features: "+str(len(loc)))

# make sift descriptors
D = sift(gry,loc)
print("number of descriptors: "+str(len(D)))

# showFeatures(img,loc,D)

from matching import matchSIFT
M = matchSIFT(D,D,40,40)

import cv2
from drawMatches import drawMatches
img2 = drawMatches(img,loc,img,loc,M)

io.imshow( img2,vmin=0,vmax=255,cmap="gray")
io.show()

#io.imshow((img * 255).astype(np.uint8)  , vmin=0, vmax=255, cmap="gray")
#io.show()
#io.imsave("out.png",img)
















