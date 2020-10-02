import cv2
import rgb2gray
import convolution
import sys
import gausskernel


if __name__ == '__main__':
	f = 'mandril_color.tif'
	f = rgb2gray.rgb1gray(f)
	w = gausskernel.gaussKernel(8, 50)
	convolution.twodConv(f, w, 'replicate')
	src = cv2.imread(f)
	cv_gaussianBlur = cv2.GaussianBlur(src, (31, 31), 5, None, 5)
	cv2.imshow('cv_gaussianBlur', cv_gaussianBlur)
	cv2.imwrite('cv_'+f, cv_gaussianBlur)
	cv2.waitKey(0)
	sys.exit(0)
