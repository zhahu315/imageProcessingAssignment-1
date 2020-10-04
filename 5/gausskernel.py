import math
import numpy as np
import sys
from numba import jit


@jit
def gaussKernel(sig, m=-1):
	w = np.zeros([m, m], dtype=float)
	min_m = math.ceil(3 * sig) * 2 + 1
	if 0 < m < min_m:
		print('the m is too small')
	elif m == -1:
		m = min_m
		print('m=', m)
		sum = 0
		for i in range(m):
			for j in range(m):
				w[i][j] = (1 / (2 * math.pi * (sig ** 2))) * math.exp(
					(-((i - int(m / 2)) ** 2) - ((j - int(m / 2)) ** 2)) / (2 * (sig ** 2)))
				sum += w[i][j]
		print(sum)
		for i in range(m):
			for j in range(m):
				w[i][j] /= sum
		print(w)
	else:
		sum = 0
		for i in range(m):
			for j in range(m):
				w[i][j] = (1 / (2 * math.pi * (sig ** 2))) * math.exp(
					(-((i - int(m / 2)) ** 2) - ((j - int(m / 2)) ** 2)) / (2 * (sig ** 2)))
				sum += w[i][j]
		print('sum=', sum)
		for i in range(m):
			for j in range(m):
				w[i][j] /= sum
		print(w)
	return w


if __name__ == '__main__':
	gaussKernel(5, 31)
	sys.exit(0)
