import cv2
import numpy as np
import sys


def rgb1gray(f, method='NTSC'):
	name = method+'_'+f
	a = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
	rgbimg = cv2.imread(f)
	h, w, _ = rgbimg.shape
	cv2.imshow('raw', a)
	arr = np.array(rgbimg)
	out = np.zeros([h, w], dtype=int)

	if method == 'average':
		# print(h, w, _)
		# print(arr[0, 0, 0], arr[0, 0, 1], arr[0, 0, 2])
		for i in range(0, h):
			for j in range(0, w):
				out[i, j] = round((round(arr[i, j, 0]) + round(arr[i, j, 1]) + round(arr[i, j, 2]))/3)
		# print('out=', out[0])
		cv2.imwrite(name, out)
		cv2.imshow(name, cv2.imread(name))
		cv2.waitKey(0)
	else:
		#print(h, w, _)
		#print(arr[0, 0, 0], arr[0, 0, 1], arr[0, 0, 2])
		for i in range(0, h):
			for j in range(0, w):
				out[i, j] = round(0.1140*arr[i, j, 0]+0.5870*arr[i, j, 1]+0.2989*arr[i, j, 2])
		#print('out=', out)
		cv2.imwrite(name, out)
		cv2.imshow(name, cv2.imread(name))
		cv2.waitKey(0)


if __name__ == '__main__':
	rgb1gray('mandril_color.tif', 'average')
	rgb1gray('mandril_color.tif')
	rgb1gray('lena512color.tiff', 'average')
	rgb1gray('lena512color.tiff')
	sys.exit(0)
