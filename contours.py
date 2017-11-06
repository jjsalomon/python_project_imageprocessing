import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('Carotid.jpg')
imgray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow("f",im2)
cv2.waitKey(0)
