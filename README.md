# CSC-414_P2
Project 2: Feature Detection and Matching
* [resource 1](https://cs.brown.edu/courses/csci1430/proj2/)  
* [Szeliski chapter 4.1](http://szeliski.org/Book/drafts/SzeliskiBook_20100903_draft.pdf)  

#### For the "aesthetic": 
* [markdown cheetsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

#### Gaussian Kernel 
* [gaussian kernel implementation](https://stackoverflow.com/questions/29731726/how-to-calculate-a-gaussian-kernel-matrix-efficiently-in-numpy)

#### Laplacian Kernel
* [Laplacian of Gaussian](https://homepages.inf.ed.ac.uk/rbf/HIPR2/log.htm)  
* [Bluring Masks vs Derivative Masks](https://www.tutorialspoint.com/dip/high_pass_vs_low_pass_filters.htm)  
* [Tutorialspoint Laplacian Operator](https://www.tutorialspoint.com/dip/laplacian_operator.htm)  

## Step 1: Feature Extraction - Szeliski 4.1.1
#### Harris Corner Detection
* [harris corner detection algorithm](https://en.wikipedia.org/wiki/Harris_Corner_Detector#Process_of_Harris_Corner_Detection_Algorithm[4][5][6])  
* [haishack.in](https://aishack.in/tutorials/harris-corner-detector/)  
* [py features harris](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_features_harris/py_features_harris.html#harris-corners)  

Use Sobel filter/operator to calculate Ix and Iy. (Note that here, Ix is the first derivative of I with respect to x. Also, 
Ix2 should denote the second derivative of I with respect to x. Finally, Ixy denotes computing the derivative of Ix with respect to y.

* [Robert Collins, CSE-486, Penn State slides](http://www.cse.psu.edu/~rtc12/CSE486/lecture06.pdf) - see last slide in list for helpful math explanation   
* [OpenCV Sobel Derivatives](https://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/sobel_derivatives/sobel_derivatives.html)   

#### Algorithm 4.1 (page 214)
1. Compute the horizontal and vertical derivatives of the image Ix and Iy by convolving the original image with derivatives of Gaussians (Section 3.2.3).
2. Compute the three images corresponding to the outer products of these gradients.
(The matrix A is symmetric, so only three entries are needed.)
3. Convolve each of these images with a larger Gaussian.
4. Compute a scalar interest measure using one of the formulas discussed above
5. Find local maxima above a certain threshold and report them as detected feature
point locations.

#### marking features on an image (with red dots)
[marking](https://stackoverflow.com/questions/49799057/how-to-draw-a-point-in-an-image-using-given-co-ordinate-with-python-opencv)

#### FAST Feature Detector
[FAST](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_fast/py_fast.html#fast)

## Step 2: Feature Description - Szeliski 4.1.2
MOPS Feature Descriptors:
* Szeliski, page 221  
* [Kuan-Hui Lee](https://courses.cs.washington.edu/courses/cse576/13sp/projects/project1/artifacts/ykhlee/Report.htm)  
* [slides](https://courses.cs.washington.edu/courses/cse455/09wi/Lects/lect6.pdf)

## Step 3: Feature Matching
#### SIFT
[SIFT tutorial](https://aishack.in/tutorials/implementing-sift-opencv/)


## random links and unanswered questions
[making a histogram from image gradient explanation](https://lilianweng.github.io/lil-log/2017/10/29/object-recognition-for-dummies-part-1.html)

What is a structure tensor?  
[structure tensor](https://en.wikipedia.org/wiki/Structure_tensor)  
[how it's used](https://en.wikipedia.org/wiki/Corner_detection#The_Harris_&_Stephens_/_Shi%E2%80%93Tomasi_corner_detection_algorithms)
[histogram of oriented gradients](https://www.learnopencv.com/histogram-of-oriented-gradients/)

#### I wish I would have seen this way sooooner.
*** [sweet](https://muthu.co/harris-corner-detector-implementation-in-python/)  ***  
[sweet](https://github.com/hughesj919/HarrisCorner)  
[sweet](http://www.kaij.org/blog/?p=89)  
[sweet](https://sandipanweb.wordpress.com/2017/10/22/feature-detection-with-harris-corner-detector-and-matching-images-with-feature-descriptors-in-python/)












