import cv2
import numpy as np
import sys
import time
from numba import jit


@jit
def twodConv(f, w, method='zero'):
	name = method + '_' + f
	row_w, column_w = w.shape
	gray_img = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
	arr_img = np.array(gray_img)
	row_img, column_img = arr_img.shape
	out_arr = np.zeros([row_img, column_img], int)
	padding_img = np.zeros([row_img + row_w - 1, column_img + column_w - 1], int)
	row_padding_img, column_padding_img = padding_img.shape

	# 矩阵翻转180度
	temp = np.zeros([row_w, column_w], float)
	for i in range(row_w):
		for j in range(column_w):
			temp[i][j] = w[row_w-i-1][column_w-j-1]
	w = temp
	print('w180=', w)

	# 填补中间
	for i in range(int(row_w / 2), row_img + int(row_w / 2)):
		for j in range(int(column_w / 2), column_img + int(column_w / 2)):
			padding_img[i, j] = arr_img[i - int(row_w / 2), j - int(column_w / 2)]

	if method == 'replicate':
		# 填补四个角
		for i in range(0, int(row_w / 2)):
			for j in range(0, int(column_w / 2)):
				padding_img[i, j] = arr_img[0, 0]
		for i in range(row_padding_img - int(row_w / 2), row_padding_img):
			for j in range(0, int(column_w / 2)):
				padding_img[i, j] = arr_img[row_img - 1, 0]
		for i in range(0, int(row_w / 2)):
			for j in range(column_padding_img - int(column_w / 2), column_padding_img):
				padding_img[i, j] = arr_img[0, column_img - 1]
		for i in range(row_padding_img - int(row_w / 2), row_padding_img):
			for j in range(column_padding_img - int(column_w / 2), column_padding_img):
				padding_img[i, j] = arr_img[row_img - 1, column_img - 1]
		print('a=', arr_img)
		# 填补四条边
		# 上边
		for i in range(0, int(row_w / 2)):
			for j in range(int(column_w / 2), column_padding_img - int(column_w / 2)):
				padding_img[i, j] = arr_img[0, j - int(column_w / 2)]
		# 下边
		for i in range(row_padding_img - int(row_w / 2), row_padding_img):
			for j in range(int(column_w / 2), column_padding_img - int(column_w / 2)):
				padding_img[i, j] = arr_img[row_img - 1, j - int(column_w / 2)]
		# 左边
		for i in range(int(row_w / 2), row_padding_img - int(row_w / 2)):
			for j in range(0, int(column_w / 2)):
				padding_img[i, j] = arr_img[i - int(row_w / 2), 0]
		# 右边
		for i in range(int(row_w / 2), row_padding_img - int(row_w / 2)):
			for j in range(column_padding_img - int(column_w / 2), column_padding_img):
				padding_img[i, j] = arr_img[i - int(row_w / 2), column_img - 1]
		for i in range(row_img):
			for j in range(column_img):
				temp = padding_img[i:i+row_w, j:j+column_w]
				temp = np.multiply(temp, w)
				out_arr[i][j] = temp.sum()
		g = cv2.imwrite(name, out_arr)
		cv2.imshow(name, cv2.imread(name))

	else:
		for i in range(row_img):
			for j in range(column_img):
				temp = padding_img[i:i+row_w, j:j+column_w]
				temp = np.multiply(temp, w)
				out_arr[i][j] = temp.sum()
		cv2.imwrite(name, out_arr)
		cv2.imshow(name, cv2.imread(name))

	g = out_arr
	return g


if __name__ == '__main__':
	a = [[-2, -4, -4, -4, -2], [-4, 0, 8, 0, -4], [-4, 8, 24, 8, -4], [-4, 0, 8, 0, -4], [-2, -4, -4, -4, -2]]
	w = np.asarray(a)
	print(w)
	twodConv('mandril_color.tif', w, 'replicate')
	print(time.process_time())
	sys.exit(0)
