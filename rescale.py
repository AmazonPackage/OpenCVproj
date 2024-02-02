import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    #Images, Videos & Live vids
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

"""def changeRes(width,height):
    #live vid only
    capture.set(3,width)
    capture.set(4,height)"""

capture = cv.VideoCapture("Videos/dog.mp4")
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)
    
    cv.imshow("Video Resized", frame_resized)

    if cv.waitKey(20) & 0xFF==ord("d"): #if letter D is pressed
        break

capture.release()
cv.destoryAllWindows()