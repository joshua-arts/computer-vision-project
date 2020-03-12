import cv2
import numpy as np
import pdb

def get_lines(img):
    # Apply edge detection method on the image
    edges = cv2.Canny(img ,100, 200, apertureSize = 3)
    minLineLength = 10
    maxLineGap = 50
    # Use probabilistic high transform to find all the lines
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength, maxLineGap)
    return lines

# Sort lines by horizontal position (left to right)
def sort_lines(lines):
    return sorted(lines, key=lambda lines: lines[0][0])

def get_line_height(line):
    (x1,y1,x2,y2) = line[0]
    return np.abs(y1-y2)


if __name__ == "__main__":
    img = cv2.imread('image.jpg')
    lines = get_lines(img)
    lines = sort_lines(lines)

    max_length = (get_line_height(lines[0]) + get_line_height(lines[1]))/2
    print(max_length)

    for line in lines:
        for x1,y1,x2,y2 in line:
            print("drawing at: ", x1, y1, " to :", x2, y2, "length: ", get_line_height(line))
            cv2.line(img,(x1,y1), (x2,y2), (0,0,255),2)
    cv2.imwrite('linesDetected.jpg', img)
