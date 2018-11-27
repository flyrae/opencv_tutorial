import cv2
import numpy as np

drawing = False
mode = True

ix,iy = -1,-1

def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_LBUTTONDOWN:
        if  drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),3,(0,0,255),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(True):
    cv2.imshow('image',img)
    k = cv2.waitKey(1)&0xFF
    if k == ord('m'):
        m = not mode
    elif k == 27:
        break