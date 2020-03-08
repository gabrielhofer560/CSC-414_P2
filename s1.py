### Step 1: Feature Extraction
from conv import imfilter
from gauss import gauss

# Compute the horizontal and vertical derivatives of the image Ix and Iy by convolving the original image with derivatives of Gaussians (Section 3.2.3).

# define sobel kernels
xsobel = [
    [1,0,-1],
    [2,0,-2],
    [1,0,-1]]

ysobel = [
    [1,2,1],
    [0,0,0],
    [-1,-2,-1]]

def extractFeatures(img):
  # get img's shape and dimensions

  H = [[0,0],[0,0]]

  # create Ixy, Iyx, Ix2, Iy2
  Ix2 = imfilter(img,xsobel)
  Ix2 = imfilter(Ix2,xsobel)

  Iy2 = imfilter(img,xsobel)
  Iy2 = imfilter(Iy2,xsobel)

  Iyx = imfilter(img,ysobel)
  Iyx = imfilter(Iyx,xsobel)

  Ixy = imfilter(img,ysobel)
  Ixy = imfilter(Ixy,xsobel)

  # create w (gaussian mask) by calling gauss from gauss.py 
  w = gauss(3,3,1)

  # calculate H 
  for x in range(r):
    for y in range(c):
       

  # create thresholding function for cornerj c(H)
  


