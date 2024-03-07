
import cv2 as cv
import sys

img_rgb = cv.imread('../assets/fox.jpg')


while True:
    ch = cv.waitKey()
    if ch == 27:
        break
    cv.imshow('fox', img_rgb)

