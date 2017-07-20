# -*- coding: utf-8 -*-
import cv2
import numpy as np
import data_path

def grey_to_color():
	img_r = cv2.imread(data_path.image_r_path)
	img_g = cv2.imread(data_path.image_g_path)
	img_b = cv2.imread(data_path.image_b_path)
	row = img_r.shape[0]
	col = img_r.shape[1]
	img = np.empty((row,col,3),dtype="uint8")

	for i in range(row):
		for j in range(col):
			img[i][j][0] = img_r[i][j][0]
			img[i][j][1] = img_g[i][j][0]
			img[i][j][2] = img_b[i][j][0]
	cv2.imwrite(data_path.BM3D_image_path, img)

if __name__ == '__main__':
	grey_to_color()
	
