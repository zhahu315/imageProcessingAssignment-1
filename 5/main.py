import cv2
import rgb2gray
import convolution
import sys
import gausskernel

f = 'cameraman.tif'
f = rgb2gray.rgb1gray(f)
w = gausskernel.gaussKernel(1, 7)
convolution.twodConv(f, w, 'replicate')
src = cv2.imread(f)
cv_gaussianBlur = cv2.GaussianBlur(src, (7, 7), 1, 0)
cv2.imshow('cv_gaussianBlur', cv_gaussianBlur)
cv2.imwrite('cv_'+f, cv_gaussianBlur)
cv2.waitKey(0)
sys.exit(0)