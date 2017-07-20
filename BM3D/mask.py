# -*- coding: utf-8 -*-

import numpy as np
import cv2
import data_path

img = cv2.imread(data_path.original_image_path)
row = img.shape[0]
col = img.shape[1]

mask_matrix = open(data_path.mask_path)

mask = np.empty((row,col), dtype="uint8")
for i in range(row):
	line = mask_matrix.readline()
	for j in range(col):
		mask[i][j] = int(line[2*j])
		if mask[i][j] == 0:
			img[i][j][0] = 0
			img[i][j][1] = 0
			img[i][j][2] = 0
cv2.imwrite(data_path.lost_image_path,img)

def my_mid(i,j):
	if i - 3 < 0:
		y_u = 0
	else:
		y_u = i - 3
	if i + 3 >= row:
		y_d = row - 1
	else:
		y_d = i + 3
	if j - 3 < 0:
		x_l = 0
	else:
		x_l = j - 3
	if j + 3 >= col:
		x_r = col - 1
	else:
		x_r = j + 3
	cnt = 0
	r = 0
	g = 0 
	b = 0
	for i1 in range(y_u, y_d + 1):
		for j1 in range(x_l, x_r + 1):
			if mask[i1][j1] == 1:
				cnt += 1 
				r += img[i1][j1][0]
				g += img[i1][j1][1]
				b += img[i1][j1][2]
	img[i][j][0] = r*1.0/cnt
	img[i][j][1] = g*1.0/cnt
	img[i][j][2] = b*1.0/cnt




for i in range(row):
	for j in range(col):
		if mask[i][j] == 0:
			my_mid(i, j)

cv2.imwrite(data_path.mid_image_path,img)





