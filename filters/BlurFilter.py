import cv2 as cv

image = cv.imread('../assets/free-nature-images.jpg')
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
filter_blur = [1,1]

class BlurFilter:
    while True:
        
        ch = cv.waitKey(1)
        if ch == 27:
            break
        
        image_filter_blur = cv.blur(src=image,ksize= (filter_blur))  
        cv.imshow('fox_ruido',  image_filter_blur)
    
