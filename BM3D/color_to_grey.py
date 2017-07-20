# -*- coding: utf-8 -*-
import cv2
import numpy as np
import data_path

def color_to_grey_1():
	img = cv2.imread(data_path.mid_image_path)
	row = img.shape[0]
	col = img.shape[1]
	img_r = np.empty((row,col),dtype="uint8")
	img_g = np.empty((row,col),dtype="uint8")
	img_b = np.empty((row,col),dtype="uint8")

	for i in range(row):
		for j in range(col):
			img_r[i][j] = img[i][j][0]
			img_g[i][j] = img[i][j][1]
			img_b[i][j] = img[i][j][2]

	cv2.imwrite(data_path.image_r_path, img_r)
	cv2.imwrite(data_path.image_g_path, img_g)
	cv2.imwrite(data_path.image_b_path, img_b)

def color_to_grey_2():
	img = cv2.imread(data_path.BM3D_image_path)
	row = img.shape[0]
	col = img.shape[1]
	img_r = np.empty((row,col),dtype="uint8")
	img_g = np.empty((row,col),dtype="uint8")
	img_b = np.empty((row,col),dtype="uint8")

	for i in range(row):
		for j in range(col):
			img_r[i][j] = img[i][j][0]
			img_g[i][j] = img[i][j][1]
			img_b[i][j] = img[i][j][2]

	cv2.imwrite(data_path.image_r_path, img_r)
	cv2.imwrite(data_path.image_g_path, img_g)
	cv2.imwrite(data_path.image_b_path, img_b)



