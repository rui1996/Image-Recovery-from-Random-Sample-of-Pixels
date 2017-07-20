import cv2
import numpy as np
import math
import data_path
#import sys
#f1 = sys.argv[1]
#f2 = sys.argv[2]

def psnr():
	img1 = np.array(cv2.cvtColor(cv2.imread(data_path.BM3D_image_path), cv2.COLOR_BGR2YCR_CB))
	img2 = np.array(cv2.cvtColor(cv2.imread(data_path.original_image_path), cv2.COLOR_BGR2YCR_CB))
	mse = np.mean((img1-img2)**2)
	print('mse : %.4f' % mse)
	if mse == 0:
		print 100
	PIXEL_MAX = 255.0
	print 20*math.log10(PIXEL_MAX / math.sqrt(mse))
	print data_path.BM3D_image_path

#psnr(img1[:,:,0],img2[:,:,0])
