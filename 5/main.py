import rgb2gray
import convolution
import gausskernel

f = 'lena512color.tiff'
f = rgb2gray.rgb1gray(f)
w = gausskernel.gaussKernel(1, 7)
convolution.twodConv(f, w, 'replicate')

