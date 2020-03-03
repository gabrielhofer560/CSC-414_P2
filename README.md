# CSC-414_P2
Project 2: Feature Detection and Matching

[resource 1](https://cs.brown.edu/courses/csci1430/proj2/)

[Szeliski chapter 4.1](http://szeliski.org/Book/drafts/SzeliskiBook_20100903_draft.pdf)

## Step 1: Feature Extraction

[Harris Corner Detection](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_features_harris/py_features_harris.html#harris-corners)

[OpenCV Sobel Derivatives](https://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/sobel_derivatives/sobel_derivatives.html)

[I love you GeeksforGeeks](https://www.geeksforgeeks.org/python-corner-detection-with-harris-corner-detection-method-using-opencv/)


### Algorithm 4.1 (page 214)

1. Compute the horizontal and vertical derivatives of the image Ix and Iy by convolving the original image with derivatives of Gaussians (Section 3.2.3).

2.  Compute the three images corresponding to the outer products of these gradients.
(The matrix A is symmetric, so only three entries are needed.)

3. Convolve each of these images with a larger Gaussian.

4. Compute a scalar interest measure using one of the formulas discussed above

5. Find local maxima above a certain threshold and report them as detected feature
point locations.

## Step 2: Feature Description

## Step 3: Feature Matching


