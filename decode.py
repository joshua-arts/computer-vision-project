import cv2
import numpy as np
import pdb

img = cv2.imread('image.jpg')
# # Convert the img to grayscale
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imwrite('gray.jpg', gray)
# Apply edge detection method on the image
edges = cv2.Canny(img ,100, 200, apertureSize = 3)
minLineLength = 10
maxLineGap = 50
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength, maxLineGap)
print("Found ", len(lines), " lines")
# The below for loop runs till r and theta values
# are in the range of the 2d array
for line in lines:
    for x1,y1,x2,y2 in line:
        print("drawing at: ", x1, y2, " to :", x2,y2)
        cv2.line(img,(x1,y1), (x2,y2), (0,0,255),2)
# All the changes made in the input image are finally
# written on a new image houghlines.jpg
cv2.imwrite('linesDetected.jpg', img)
