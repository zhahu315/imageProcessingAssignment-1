import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt


def scanLine4e(f, I, loc):
	name = loc + '_' + f
	img_name = []
	img_name.insert(-1, name[:-3]+'jpg')
	img_name = ''.join(img_name)
	print(name)
	# print(img_name)
	if loc == 'row':
		grayImage = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
		arr = np.array(grayImage)
		h, w = grayImage.shape
		# print(h, w)
		I = int(h/2)
		# print(arr[:, 0])
		out = arr[I-1, :]
		# print(out.shape)
		cv2.imwrite(name, out)
		x = range(w)
		# print(x)
		plt.plot(x, out)
		plt.title(name)
		plt.xlabel('row')
		plt.ylabel('gray_scale')
		plt.savefig(img_name, dpi=100)
		plt.show()
		return out

	if loc == 'column':
		grayImage = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
		arr = np.array(grayImage)
		h, w = grayImage.shape
		I = int(w/2)
		# print(grayImage)
		out = arr[:, I-1]
		# print(out.shape)
		cv2.imwrite(name, out)
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
