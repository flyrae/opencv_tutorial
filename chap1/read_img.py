# -*- coding: utf-8 -*-


import numpy as numpy
import cv2
from matplotlib import pyplot as plt 

img = cv2.imread("../image/lena.jpg",0)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img,cmap="gray",interpolation='bicubic')
plt.xticks([]),plt.yticks([])
plt.show()