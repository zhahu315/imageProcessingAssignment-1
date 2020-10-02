import math
import numpy as np
import sys
import cv2 as cv
from conv import Conv


def gaussKernel(sig, m=-1):
	min_m = math.ceil(3 * sig) * 2 + 1
	if m == -1:
		m = min_m
		print(m)
	elif 0 < m < min_m:
		print('the m is too small')
	else:
		w = np.zeros([m, m], dtype=float)
		sum = 0.
		for i in range(m):
			for j in range(m):
				w[i][j] = (1 / (2 * math.pi * sig))\
				* (math.exp(-pow((j-int(m/2)), 2)\
				-pow(i-int(m/2), 2)\
				/(2*pow(sig, 2))))
				sum += w[i][j]
		for i in range(m):
			for j in range(m):
				w[i][j] /= sum
		print(w)
	Conv.twodConv('1.2.06.tiff', w, 'replicate')


if __name__ == '__main__':
	gaussKernel(3, 19)
	sys.exit(0)
