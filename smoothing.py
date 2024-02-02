import cv2 as cv

img = cv.imread("Photos/cats.jpg")

#Averaging
average = cv.blur(img, (7,7))
cv.imshow("Average Blur", average)

#Gaussian
gaussian = cv.GaussianBlur(img, (7,7), 0)
cv.imshow("Gaussian Blur", gaussian)

#Median
median = cv.medianBlur(img, 7) #opencv assumes this as 7x7
cv.imshow("Median Blur", median)

#Bilateral
bilateral = cv.bilateralFilter(img, 7, 35, 15) #sigmaspace: pixels further out will affect blurring calculation
cv.imshow("Bilateral", bilateral)

cv.waitKey(0)