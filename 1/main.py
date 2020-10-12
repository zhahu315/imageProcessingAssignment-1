import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt


def scanLine4e(f, I, loc):
	# 图像命名，使输出的折线图后缀改为.jpg
	name = loc + '_' + f
	img_name = []
	img_name.insert(-1, name[:-3]+'jpg')
	img_name = ''.join(img_name)
	# 读取灰度图
	grayImage = cv2.imread(f, cv2.IMREAD_GRAYSCALE)

	# 当loc为行时
	if loc == 'row':
		# 将灰度图读入数组
		arr = np.array(grayImage)
		# 得到行数列数
		h, w = grayImage.shape
		# print(h, w)
		# 确定中间行
		I = int(h/2)
		# print(arr[:, 0])
		# 输出中间行并且画出折线图
		out = arr[I-1, :]
		# print(out.shape)
		cv2.imwrite(name, out)
		# 将得到的序列画为折线图
		x = range(w)
		# print(x)
		plt.plot(x, out)
		plt.title(name)
		plt.xlabel('row')
		plt.ylabel('gray_scale')
		plt.savefig(img_name, dpi=100)
		plt.show()
		return out
	# 列操作同上
	if loc == 'column':
		arr = np.array(grayImage)
		h, w = grayImage.shape
		I = int(w/2)
		# print(grayImage)
		out = arr[:, I-1]
		# print(out.shape)
		cv2.imwrite(name, out)
		# 将得到的序列画为折线图
		x = range(h)
		plt.plot(x, out)
		plt.title(name)
		plt.xlabel('column')
		plt.ylabel('gray_scale')
		plt.savefig(img_name, dpi=100)
		plt.show()
		return out


if __name__ == '__main__':
	print(scanLine4e('cameraman.tif', 0, 'row'))
	print(scanLine4e('cameraman.tif', 0, 'column'))
	print(scanLine4e('einstein.tif', 0, 'row'))
	print(scanLine4e('einstein.tif', 0, 'column'))
	sys.exit(0)
