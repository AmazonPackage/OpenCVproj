import cv2 as cv

img = cv.imread("Photos/park.jpg")
cv.imshow("Park", img)

#grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

#blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

#edge cascade
canny = cv.Canny(blur,125,175)
cv.imshow("Canny Edges", canny)

#dilating the image
dilated = cv.dilate(canny, (5,5), iterations=3)
cv.imshow("Dilate", dilated)

#erode
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow("Eroded", eroded)

#resize
resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resize)

#cropping
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0) 