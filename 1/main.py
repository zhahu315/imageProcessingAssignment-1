import cv2
import numpy as np
import sys

def scanLine4e(f, I, loc):
	name = loc + '_' + f
	print(name)
	if loc == 'row':
		grayImage = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
		arr = np.array(grayImage)
		h, w = grayImage.shape
		I = int(h/2)
		#print(arr[:, 0])
		out = arr[I-1:I, :]
		#print(out)
		cv2.imwrite(name, out)
		cv2.imshow(name, out)
		cv2.waitKey(0)
		return out

	if loc == 'column':
		grayImage = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
		arr = np.array(grayImage)
		h, w = grayImage.shape
		I = int(w/2)
		#print(grayImage)
		out = arr[:, I-1]
		#print(out)
		cv2.imwrite(name, out)
		cv2.imshow(name, out)
		cv2.waitKey(0)
		return out

if __name__ =='__main__':
	print(scanLine4e('cameraman.tif', 0, 'row'))
	print(scanLine4e('cameraman.tif', 0, 'column'))
	print(scanLine4e('einstein.tif', 0, 'row'))
	print(scanLine4e('einstein.tif', 0, 'column'))
	sys.exit(0)
