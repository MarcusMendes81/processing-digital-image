
import cv2 as cv
import sys

img_rgb = cv.imread('../assets/fox.jpg')
img_gray = cv.cvtColor(img_rgb,cv.COLOR_BGR2GRAY)
filter_median = cv.medianBlur(img_gray, 5)

while True:
    ch = cv.waitKey(1)
   
    if ch == 27:
        break    
    cv.imshow('fox', filter_median)
   
    
