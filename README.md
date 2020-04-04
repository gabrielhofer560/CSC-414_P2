**Project 2: Feature Detection and Matching**

Author: Gabriel Hofer

CSC-414 Introduction to Computer Vision

Instructor: Dr. Hoover

April 4, 2020

Computer Science and Engineering\
South Dakota School of Mines and Technology\

**Step 1: Feature Extraction**\
I implemented the Harris Corner Detection algorithm for feature
extraction.\
**Step 2: Descriptors**\
I implemented a [Histogram of Oriented Gradients
(HOG)](https://en.wikipedia.org/wiki/Histogram_of_oriented_gradients)
for the feature descriptor. For each Keypoint, K, we create a 16x16
window around centered at K. Then, we partition this 16x16 window into
16 4x4 sub-windows. For each 4x4 sub-window, we compute and apply a
Laplacian filter to the image:
$$L(x,y,\sigma) = G(x,y,\sigma) * I(x,y)$$ For each cell in the 4x4
subwindow, we compute the magnitude, $m(x,y)$, and orientation
$ \theta (x,y) $ of the cell with respect to the center of the window.
$$m(x,y) = \sqrt{(L(x+1,y)-L(x-1,y))^2+(L(x,y+1)-L(x,y-1))^2}$$
$$\theta (x,y) = \arctan{(L(x,y+1)-L(x,y-1))/(L(x+1,y)-L(x-1,y))}$$ An
8-bin histogram is constructed to determine the orientation of the whole
4x4 subwindow. Each cell is assigned to one of the bins based on it’s
orientation ($\theta$). The magnitude of the cell is added to its bin.
The orientation of the histogram is determined by the largest bin in the
histogram. Once a histogram has been made for each of the 16 4x4
subwindows, a histogram of oriented gradients is made for the 16x16
window using the results from the 4x4 subwindows. Specifically, each 4x4
histogram acts like a single cell in the 16x16 window. The magnitude of
each 4x4 window is added to the appropriate bin in the 16x16 histogram
based on the orientation of the 4x4 window. Finally, the orientation and
mangitude of the 16x16 window is determined by the largest bin in the
histogram.\
**Step 3: Feature Matching**\
My feature matching algorithm looks at all pairs of feature descriptors,
$(d0,d1)$.

A pair becomes a match if it meets two criteria:

1.  the difference of orientations between d0 and d1 is less than the
    orientation threshold

2.  the difference of magnitude between d0 and d1 is less than the
    magnitude threshold

For drawing the matches between the two descriptors, I used a [digital
differential analyzer
(DDA)](https://en.wikipedia.org/wiki/Digital_differential_analyzer_(graphics_algorithm))
algorithm.
