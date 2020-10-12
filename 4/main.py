import math
import numpy as np
import sys
import matplotlib.pyplot as plt

def gaussKernel(sig, m=-1):
	# 未设定参数情况下默认m为-1
	# 初始化卷积核
	w = np.zeros([m, m], dtype=float)
	# 确定卷积核尺度m的最小值
	min_m = math.ceil(3 * sig) * 2 + 1
	# m过小则报错
	if 0 < m < min_m:
		print('the m is too small')
	# 未传递参数则将m设定为最小值
	elif m == -1:
		m = min_m
		print('m=', m)
		# 初始化和
		sum = 0
		# 计算高斯核，并累加
		for i in range(m):
			for j in range(m):
				w[i][j] = (1 / (2 * math.pi * (sig ** 2))) * math.exp(
					(-((i - int(m / 2)) ** 2) - ((j - int(m / 2)) ** 2)) / (2 * (sig ** 2)))
				sum += w[i][j]
		print(sum)
		# 归一化
		for i in range(m):
			for j in range(m):
				w[i][j] /= sum
		print(w)
	# m满足条件的情况下
	else:
		#初始化归一化的和
		sum = 0
		# 计算高斯核树枝，并累加
		for i in range(m):
			for j in range(m):
				w[i][j] = (1 / (2 * math.pi * (sig ** 2))) * math.exp(
					(-((i - int(m / 2)) ** 2) - ((j - int(m / 2)) ** 2)) / (2 * (sig ** 2)))
				sum += w[i][j]
		# 归一化
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
