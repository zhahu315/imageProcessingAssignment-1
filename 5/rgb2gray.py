import cv2
import numpy as np
import sys
# from numba import jit


# @jit
def rgb1gray(f, method='NTSC'):
	name = method+'_'+f
	a = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
	cv2.imshow('raw', a)
	if method == 'average':
		rgbimg = cv2.imread(f)
		h, w, _ = rgbimg.shape
		#print(h, w, _)
		arr = np.array(rgbimg)
		#print(arr[0, 0, 0], arr[0, 0, 1], arr[0, 0, 2])
		out = np.zeros([h, w], dtype=int)
		for i in range(0, h):
			for j in range(0, w):
				out[i, j] = round((arr[i, j, 0] + arr[i, j, 1] + arr[i, j, 2])/3)
		#print('out=', out)
		grayimg = cv2.imwrite(name, out)
		print(grayimg)
		#cv2.namedWindow(name, cv2.WINDOW_FREERATIO)
		cv2.imshow(name, cv2.imread(name))
		cv2.waitKey(1000)
	else:
		rgbimg = cv2.imread(f)
		h, w, _ = rgbimg.shape
		#print(h, w, _)
		arr = np.array(rgbimg)
		#print(arr[0, 0, 0], arr[0, 0, 1], arr[0, 0, 2])
		out = np.zeros([h, w], dtype=int)
		for i in range(0, h):
			for j in range(0, w):
				out[i, j] = round(0.1140*arr[i, j, 0]+0.5870*arr[i, j, 1]+0.2989*arr[i, j, 2])
		#print('out=', out)
		grayimg = cv2.imwrite(name, out)
		#cv2.namedWindow(name, cv2.WINDOW_FREERATIO)
		cv2.imshow(name, cv2.imread(name))
		cv2.waitKey(1000)
	return name

if __name__ == '__main__':
	rgb1gray('mandril_color.tif', 'average')
	rgb1gray('mandril_color.tif')
	rgb1gray('lena512color.tiff', 'average')
	rgb1gray('lena512color.tiff')
	sys.exit(0)
