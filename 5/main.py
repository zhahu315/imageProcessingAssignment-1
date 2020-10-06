import cv2
import rgb2gray
import convolution
import sys
import numpy as np
import gausskernel


if __name__ == '__main__':
	f = 'mandril_color.tif'
	f = rgb2gray.rgb1gray(f)
	w = gausskernel.gaussKernel(5, 31)
	g = convolution.twodConv(f, w, 'replicate')
	src = cv2.imread(f)
	cv_gaussianBlur = cv2.GaussianBlur(src, (31, 31), 5, None, 5)
	cv2.imshow('cv_gaussianBlur', cv_gaussianBlur)
	# 计算差值图像并输出
	difference = np.zeros((g.shape[0], g.shape[1]), int)
	for i in range(g.shape[0]):
		for j in range(g.shape[1]):
			difference[i][j] = abs(g[i][j] - cv_gaussianBlur[i][j][0])
	print('difference=', difference)
	cv2.imwrite('difference.tif', difference)
	cv2.imshow('difference', cv2.imread('difference.tif'))
	cv2.imwrite('cv_'+f, cv_gaussianBlur)
	cv2.waitKey(0)
	sys.exit(0)
