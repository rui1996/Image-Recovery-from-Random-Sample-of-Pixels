# -*- coding: utf-8 -*-
import cv2

image_name = "kodim05"
rate = "40"
mask_name = "mask_kodim05_" + rate + ".txt"
original_image_path = "/home/qianrui/BM3D/data/" + image_name + ".jpg"
BM3D_image_path = "/home/qianrui/BM3D/data/" + image_name + "_" + rate + "_BM3D.jpg"
lost_image_path = "/home/qianrui/BM3D/data/" + image_name + "_change.jpg"
mid_image_path = "/home/qianrui/BM3D/data/" + image_name + "_mid.jpg"
image_r_path = "/home/qianrui/BM3D/data/" + image_name + "_r.jpg"
image_g_path = "/home/qianrui/BM3D/data/" + image_name + "_g.jpg"
image_b_path = "/home/qianrui/BM3D/data/" + image_name + "_b.jpg"
mask_path = "/home/qianrui/BM3D/data/" + mask_name +".txt"
