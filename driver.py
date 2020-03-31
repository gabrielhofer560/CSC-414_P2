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


img = io.imread(sys.argv[1]);
cpy = img
gry = rgb2gray(img)



loc = harris(gry,gk(3,3,1),0.03)
print("number of features: "+str(len(loc)))
showDots(img,loc)

#exit()

D = sift(gry,loc)

#for i in range(20):
#    print("i: "+str(i)+" = "+str(D[i][0])+"  "+str(D[i][1]))

showFeatures(img,loc,D)




#io.imshow((img * 255).astype(np.uint8)  , vmin=0, vmax=255, cmap="gray")
#io.show()
#io.imsave("out.png",img)






