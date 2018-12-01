import numpy as np
import argparse
import cv2

def translate(image, x, y):
    M = np.float32([[1,0,x],[0,1,y]])
    shifted = cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
    return shifted

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image")
args = vars(ap.parse_args())


image = cv2.imread(args["image"])

cv2.imshow('Original',image)

shifted = translate(image,0,100)
cv2.imshow('Shifted Down', shifted)

shifted = translate(image,0,-100)
cv2.imshow("Shifted Up",shifted)

shifted = translate(image,50,0)
cv2.imshow('Shifted Right',shifted)\

shifted = translate(image,-50,0)
cv2.imshow("Shifted Left",shifted)

cv2.waitKey(0)