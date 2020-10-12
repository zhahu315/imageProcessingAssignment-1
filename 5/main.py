import cv2
import rgb2gray
import sys
import numpy as np
import convolution
import gausskernel
import matplotlib.pyplot as plt

# 将之前写好的函数分别封装到几个文件中，在主函数中调用


if __name__ == '__main__':
	f = 'lena512color.tiff'
	f = rgb2gray.rgb1gray(f)
	w = gausskernel.gaussKernel(1, 7)
	g = convolution.twodConv(f, w, 'replicate')

	# g_2 = convolution.twodConv(f, w)
	
	# 计算与系统函数差值
	# src = cv2.imread(f)
	# cv_gaussianBlur = cv2.GaussianBlur(src, (7, 7), 1, None, 1)
	# cv2.imshow('cv_gaussianBlur', cv_gaussianBlur)
	# # 计算差值图像并输出
	# difference = np.zeros((g.shape[0], g.shape[1]), int)
	# for i in range(g.shape[0]):
	# 	for j in range(g.shape[1]):
	# 		# difference[i][j] = abs(g[i][j] - cv_gaussianBlur[i][j][0])
	# 		difference[i][j] = (g[i][j] - g_2[i][j])
	# print('difference=', difference)
	#
	# cv2.imwrite('difference.tif', difference)
	# cv2.imshow('difference', cv2.imread('difference.tif'))
	# # cv2.imwrite('cv_'+f, cv_gaussianBlur)
	# cv2.waitKey(0)

	# 画出差值分布图像
	# fig = plt.figure()
	# ax = fig.add_subplot(111, projection='3d')
	# x = range(g.shape[0])
	# y = range(g.shape[1])
	# Z = difference[x][y]
	# X, Y = np.meshgrid(x, y)
	# ax.plot_surface(X, Y, Z, cmap='rainbow')
	# plt.show()

	sys.exit(0)
