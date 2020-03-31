"""
Author: Gabriel Hofer
Course: CSC-414
Instructor: Dr. Randy Hoover
"""
from imfilter import imfilter
from gk import gk
from harris import harris
from showFeatures import showFeatures
import numpy as np
import sys
from skimage import io
from skimage.color import rgb2gray


img = io.imread(sys.argv[1]);
cpy = img
gry = rgb2gray(img)

feat = harris(gry,gk(3,3,1),0.4)
print("number of features: "+str(len(feat)))
showFeatures(img,feat)



import dscr

D = sift(img,feat)

# showFeatures2()






#io.imshow((img * 255).astype(np.uint8)  , vmin=0, vmax=255, cmap="gray")
#io.show()
#io.imsave("out.png",img)



