import cv2
import numpy as np
import sys
import time


def twodConv(f, w, method='zero'):
	# 将输出图像命名
	name = method + '_' + f
	# 获取卷积核的行数，列数
	row_w, column_w = w.shape
	# 读取灰度图像
	gray_img = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
	# 将图像载入数组
	arr_img = np.array(gray_img)
	# 得到图像的行列数
	row_img, column_img = arr_img.shape
	# 初始化卷积后的图像数组
	out_arr = np.zeros([row_img, column_img], int)
	# 初始化填补边缘的图像数组
	padding_img = np.zeros([row_img + row_w - 1, column_img + column_w - 1], int)
	# 获取填补数组的行列数
	row_padding_img, column_padding_img = padding_img.shape

	# 卷积核矩阵翻转180度
	temp = np.zeros([row_w, column_w], float)
	for i in range(row_w):
		for j in range(column_w):
			temp[i][j] = w[row_w-i-1][column_w-j-1]
	w = temp
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
		# 填补中间
		for i in range(int(row_w / 2), row_img + int(row_w / 2)):
			for j in range(int(column_w / 2), column_img + int(column_w / 2)):
				padding_img[i, j] = arr_img[i - int(row_w / 2), j - int(column_w / 2)]
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
	a = [[1/25, 1/25, 1/25, 1/25, 1/25], [1/25, 1/25, 1/25, 1/25, 1/25], [1/25, 1/25, 1/25, 1/25, 1/25], [1/25, 1/25, 1/25, 1/25, 1/25], [1/25, 1/25, 1/25, 1/25, 1/25]]
	# a = [[-2, -4, -4, -4, -2], [-4, 0, 8, 0, -4], [-4, 8, 24, 8, -4], [-4, 0, 8, 0, -4], [-2, -4, -4, -4, -2]]
	w = np.asarray(a)
	print(w)
	twodConv('einstein.tif', w)
	print(time.process_time())
	sys.exit(0)
