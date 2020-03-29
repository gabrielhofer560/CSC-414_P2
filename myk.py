import numpy as np
import math

def gkern(r,c,s):
	arr=np.zeros((r,c))
	for i in range(r):
		for j in range(c):
			#print((1/(2*math.pi*s*s)))
			#print(math.exp(-1*(r*r+c*c)/(2*s*s)))
			arr[i,j]=(1/(2*math.pi*s*s))*math.exp(-1*((i-r//2)*(i-r//2)+(j-c//2)*(j-c//2))/(2*s*s))
	return arr



