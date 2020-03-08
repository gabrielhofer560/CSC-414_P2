import numpy as np
import math

## https://www.geeksforgeeks.org/gaussian-filter-generation-c/
def gauss(r, c, sigma):
  k=np.zeros((r,c))
  if r<3 or c<3:
    return []
  if r%2==0: r-=1
  if c%2==0: c-=1
  rows,cols=r,c
  s=2.0*sigma*sigma
  (cr,cc)=(r//2,c//2)
  sum=0.0
  for i in range(-cr,cr+1):
    for j in range(-cc,cc+1):
      r=math.sqrt(i*i+j*j)
      k[i+cr][j+cc]=math.exp(-r*r/s)/(math.pi*s) 
      sum+=k[i+cr][j+cc]
  for i in range(rows):
    for j in range(cols):
      k[i][j]/=sum
  return k


