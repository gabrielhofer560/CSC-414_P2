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
gry = rgb2gray(img)

# get list of locations of interest points
loc = harris(gry,gk(3,3,1),0.1)
print("number of features: "+str(len(loc)))

# make sift descriptors
D = sift(gry,loc)
showFeatures(img,loc,D)


#io.imshow((img * 255).astype(np.uint8)  , vmin=0, vmax=255, cmap="gray")
#io.show()
#io.imsave("out.png",img)






