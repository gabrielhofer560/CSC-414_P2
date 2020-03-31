"""
Author: Gabriel Hofer
Course: CSC-414
Instructor: Dr. Randy Hoover
"""
"""
https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
https://stackoverflow.com/questions/49643907/clipping-input-data-to-the-valid-range-for-imshow-with-rgb-data-0-1-for-floa
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
img = rgb2gray(img)

feat = harris(img,gk(3,3,1),0.4)
print(len(feat))
showFeatures(cpy,feat)


#io.imshow((img * 255).astype(np.uint8)  , vmin=0, vmax=255, cmap="gray")
#io.show()
#io.imsave("out.png",img)



