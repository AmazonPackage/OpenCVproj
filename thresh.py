import cv2 as cv

img = cv.imread("Photos/cats.jpg")
cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

#Simple Thresholding
threshold, thresh = cv.threshold(gray, 170, 255, cv.THRESH_BINARY)
cv.imshow("Simple Threshold", thresh)

threshold, thresh = cv.threshold(gray, 170, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple Threshold Inverse", thresh)

#Adaptive Thresholding
adapative_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 15, 2)
cv.imshow("Adpative Thresholding", adapative_thresh)


cv.waitKey(0)