# CSC-414_P2
Project 2: Feature Detection and Matching

[resource 1](https://cs.brown.edu/courses/csci1430/proj2/)  
[Szeliski chapter 4.1](http://szeliski.org/Book/drafts/SzeliskiBook_20100903_draft.pdf)  

### Markdown Cheat-Sheet
[markdown cheat-sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

### Gaussian Kernel 

[gaussian kernel implementation](https://stackoverflow.com/questions/29731726/how-to-calculate-a-gaussian-kernel-matrix-efficiently-in-numpy)

### Laplacian Kernel

[Laplacian of Gaussian](https://homepages.inf.ed.ac.uk/rbf/HIPR2/log.htm)
[Bluring Masks vs Derivative Masks](https://www.tutorialspoint.com/dip/high_pass_vs_low_pass_filters.htm),
[tutorialspoint laplacian operator](https://www.tutorialspoint.com/dip/laplacian_operator.htm)  

## Step 1: Feature Extraction

[Harris Corner Detection](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_features_harris/py_features_harris.html#harris-corners)

Use Sobel filter/operator to calculate Ix and Iy. (Note that here, Ix is the first derivative of I with respect to x. Also, 
Ix2 should denote the second derivative of I with respect to x. Finally, Ixy denotes computing the derivative of Ix with respect to y.

[OpenCV Sobel Derivatives](https://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/sobel_derivatives/sobel_derivatives.html),
[the last slide page helped a lot](http://www.cse.psu.edu/~rtc12/CSE486/lecture06.pdf),
[harris corner detector explanation](https://aishack.in/tutorials/harris-corner-detector/),

### Algorithm 4.1 (page 214)

1. Compute the horizontal and vertical derivatives of the image Ix and Iy by convolving the original image with derivatives of Gaussians (Section 3.2.3).
2. Compute the three images corresponding to the outer products of these gradients.
(The matrix A is symmetric, so only three entries are needed.)
3. Convolve each of these images with a larger Gaussian.
4. Compute a scalar interest measure using one of the formulas discussed above
5. Find local maxima above a certain threshold and report them as detected feature
point locations.

## Step 2: Feature Description

See 4.1.2 for feature descriptors and such...

[slides](https://courses.cs.washington.edu/courses/cse455/09wi/Lects/lect6.pdf)

## Step 3: Feature Matching


