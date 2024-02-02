import cv2 as cv
import numpy as np

img = cv.imread("Photos/park.jpg")

blank = np.zeros(img.shape[:2], dtype="uint8")

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank,blank,r])

cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)

print(img.shape) #3 represents no. of colour channels
print(b.shape)
print(g.shape)
print(r.shape)
#Individually, b, g & r are shown as grayscale; distribution of b/g/r pixels

merged = cv.merge([b,g,r])
cv.imshow("Merged", merged)

cv.waitKey(0)