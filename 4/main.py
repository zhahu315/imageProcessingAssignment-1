import math
import numpy as np
import sys
import matplotlib.pyplot as plt


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
		for i in range(m):
			for j in range(m):
				w[i][j] /= sum
		print(w)
	return w




if __name__ == '__main__':
	w = gaussKernel(5, 31)
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	x = range(31)
	y = range(31)
	Z = w[x][y]
	X, Y = np.meshgrid(x, y)
	ax.plot_surface(X, Y, Z, cmap='rainbow')
	plt.show()
	sys.exit(0)
