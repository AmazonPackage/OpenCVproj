import cv2 as cv

"""img = cv.imread("Photos/cat_large.jpg")

cv.imshow("Cat", img) #"Cat" being the title bar"""

#Reading Vids

capture = cv.VideoCapture("videos/dog.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF==ord("d"): #if letter D is pressed
        break

capture.release
cv.waitKey(0)