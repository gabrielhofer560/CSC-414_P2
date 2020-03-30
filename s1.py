"""
Step 1: Feature Extraction
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
img = rgb2gray(img)
io.imshow(img)
io.show()
# io.imsave("out.png",img)

print(img.shape)
k = gk(3,3,1)
#img = harris(img,k,3,200)
img = harris(img,k,3,0.003)
io.imshow((img * 255).astype(np.uint8)  , vmin=0, vmax=255, cmap="gray")
io.show()





