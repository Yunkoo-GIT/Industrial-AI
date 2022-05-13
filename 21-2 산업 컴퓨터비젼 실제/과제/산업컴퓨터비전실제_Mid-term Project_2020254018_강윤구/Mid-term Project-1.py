# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 21:40:44 2021

@author: kadmin
"""

import cv2
#import argparse
#import random
import numpy as np
import matplotlib.pyplot as plt


grey = cv2.imread('../Assignment/data/Server-6.png', 0)
image = cv2.imread('../Assignment/data/Server-6.png')


# Threshold 값 입력
in_thr = np.int(input("Input Threshold (ex:200) : "))
image_eq = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thr, mask = cv2.threshold(image_eq, in_thr, 1, cv2.THRESH_BINARY)
print('Threshole used:', thr)


# Equalize Histogram
cv2.imshow('original grey', grey)
#cv2.waitKey()

hist, bins = np.histogram(grey, 256, [0, 255])
plt.fill(hist)
plt.xlabel('pixel value')
plt.show()

grey_eq = cv2.equalizeHist(grey)
hist, bins = np.histogram(grey_eq, 256, [0, 255])
plt.fill_between(range(256), hist, 0)
plt.xlabel('pixel value')
plt.show()

cv2.imshow('equalized grey', grey_eq)
cv2.waitKey()

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hsv[..., 2] = cv2.equalizeHist(hsv[..., 2])
color_eq = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow('original color', image)
cv2.imshow('equalized color', color_eq)
cv2.waitKey()
cv2.destroyAllWindows()


# Canny Edge
def canny():
#    edge1 = cv2.Canny(grey, 50, 200)
#    edge2 = cv2.Canny(grey, 100, 200)
    edge3 = cv2.Canny(grey, 170, 200)

    cv2.imshow('original', grey)
#    cv2.imshow('Canny Edge1', edge1)
#    cv2.imshow('Canny Edge2', edge2)
    cv2.imshow('Canny Edge3', edge3)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

canny()


# Mouse로 ROI 지정
image_to_show = np.copy(image)
w, h = image.shape[1], image.shape[0]


mouse_pressed = False
s_x = s_y = e_x = e_y = -1

def mouse_callback(event, x, y, flags, param):
    global image_to_show, s_x, s_y, e_x, e_y, mouse_pressed
    
    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_pressed = True
        s_x, s_y = x, y
        image_to_show = np.copy(image)
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_pressed:
            image_to_show = np.copy(image)
            cv2.rectangle(image_to_show, (s_x, s_y), (x, y), (0, 255, 0), 2)
                    
    elif event == cv2.EVENT_LBUTTONUP:
        mouse_pressed = False
        e_x, e_y = x, y
        
cv2.namedWindow('Input ROI')
cv2.setMouseCallback('Input ROI', mouse_callback)

while True:
    cv2.imshow('Input ROI', image_to_show)
    k = cv2.waitKey(1)
    
    if k == ord('c'):
        if s_y > e_y:
            s_y, e_y = e_y, s_y
        if s_x > e_x:
            s_x, e_x = e_x, s_x
            
        if e_y - s_y > 1 and e_x - s_x > 0:
            image = image[s_y:e_y, s_x:e_x]
            image_to_show = np.copy(image)
    elif k == 27:
        break
    
cv2.destroyAllWindows()


# ROI 부분에 대한 Threshold
image_eq = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

thr, mask = cv2.threshold(image_eq, in_thr, 1, cv2.THRESH_BINARY)

plt.figure(figsize=(10, 4))
plt.subplot(121)
plt.axis('off')
plt.title('ROI image')
plt.imshow(image_eq, cmap='gray')
plt.subplot(122)
plt.axis('off')
plt.title('binary threshold')
plt.imshow(mask, cmap='gray')
plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()




