import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype="uint8")
#cv.imshow("Blank", blank)

#paint img

#blank[200:300, 300:400] = 0,255,0
#cv.imshow("Green", blank)

#2. Rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=-1)
#cv.imshow("Rectangle", blank)

#3. Circle
cv.circle(blank, (250,250), 40, (0,0,255), thickness=3)
#cv.imshow("Circle", blank)

#4. Line
cv.line(blank, (100,250), (300,450), (255,255,255), thickness=3)
#cv.imshow("Line", blank)

#5. Text
cv.putText(blank, "Hello!", (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,0), 2)
cv.imshow("Text", blank)
cv.waitKey(0)