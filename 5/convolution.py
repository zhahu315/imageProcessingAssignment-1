import cv2
import numpy as np
import sys
import time
from numba import jit


@jit
def twodConv(f, w, method='zero'):
	name = method + '_' + f
	if method == 'replicate':
		row_w, column_w = w.shape
		gray_img = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
		arr_img = np.array(gray_img)
		row_img, column_img = arr_img.shape
		out_arr = np.zeros([row_img, column_img], int)
		padding_img = np.zeros([row_img + row_w - 1, column_img + column_w - 1], int)
		# 填补中间
		for i in range(int(row_w/2), row_img+int(row_w/2)):
			for j in range(int(column_w/2), column_img+int(column_w/2)):
				padding_img[i, j] = arr_img[i-int(row_w/2), j-int(column_w/2)]
		padding_img = np.pad(arr_img, ((int(row_w/2), int(row_w/2),), (int(column_w/2), (int(column_w/2)))), 'edge')
		for i in range(row_img):
			for j in range(column_img):
				temp = padding_img[i:i+row_w, j:j+column_w]
				temp = np.multiply(temp, w)
				out_arr[i][j] = temp.sum()
		g = cv2.imwrite(name, out_arr)
		cv2.imshow(name, cv2.imread(name))
		cv2.waitKey(1000)

	else:
		row_w, column_w = w.shape
		gray_img = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
		arr_img = np.array(gray_img)
		row_img, column_img = arr_img.shape
		out_arr = np.zeros([row_img, column_img], int)
		padding_img = np.zeros([row_img + row_w - 1, column_img + column_w - 1], int)
		# 填补中间
		for i in range(int(row_w / 2), row_img + int(row_w / 2)):
			for j in range(int(column_w / 2), column_img + int(column_w / 2)):
				padding_img[i, j] = arr_img[i - int(row_w / 2), j - int(column_w / 2)]
		padding_img = np.pad(arr_img, ((int(row_w/2), int(row_w/2)), (int(column_w/2), (int(column_w/2)))))
		for i in range(row_img):
			for j in range(column_img):
				temp = padding_img[i:i+row_w][j:j+column_w]
				temp = np.multiply(temp, w)
				out_arr[i][j] = temp.sum()
		g = cv2.imwrite(name, out_arr)
		cv2.imshow(name, cv2.imread(name))
		cv2.waitKey(1000)


if __name__ == '__main__':
	# a = [[1, -1, 1, 5, 4], [-1, 5, -1, 2, 3], [1, -1, 1, -2, -1], [-1, 5, -1, 2, 3], [-1, 5, -1, 2, 3]]
	a = [[-2, -4, -4, -4, -2], [-4, 0, 8, 0, -4], [-4, 8, 24, 8, -4], [-4, 0, 8, 0, -4], [-2, -4, -4, -4, -2]]
	w = np.asarray(a)
	print(w)
	twodConv('mandril_color.tif', w, 'replicate')
	print(time.process_time())
	sys.exit(0)
