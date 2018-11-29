import cv2
import numpy as np
img = cv2.imread('../image/lena.jpg')
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))
cv2.imshow('b',b)
cv2.imshow('g',g)
cv2.imshow('r',r)
cv2.imshow('img',img)

cv2.waitKey(0)