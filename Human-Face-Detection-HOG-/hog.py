# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 21:08:24 2017

@author: umair
"""
import cv2
import numpy as np

# Python gradient calculation 
 
# Read image
im = cv2.imread('screw.bmp')
img = np.float32(im) / 255.0
 
# Calculate gradient 
gx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=1)
gy = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=1)

# Python Calculate gradient magnitude and direction ( in degrees ) 
mag, angle = cv2.cartToPolar(gx, gy, angleInDegrees=True)

print(gx)
#cv2.imshow(gx, img)