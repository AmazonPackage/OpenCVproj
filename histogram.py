
"""import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Photos/cats.jpg")
cv.imshow("Cats", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

gray = cv.cvtCOLOR(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

mask = cv.circle(blank, (img))

#Grayscale Histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(gray_hist)
plt.xlim([0,256])

cv.waitKey(0)"""