import cv2
import numpy as np

class Decoder:
    def __init__(self, image_arr):
        img = cv2.imdecode(image_arr, cv2.IMREAD_COLOR)
        self.lines = self.get_lines(img)
        self.lines = self.sort_lines()

        self.max_length = (self.get_line_length(self.lines[0]) + self.get_line_length(self.lines[1]))/2
        self.top, self.bottom = self.get_top_bottom_location(self.lines[:2])
        self.top_values = {
            0.9: "0",
            0.8: "2",
            0.7: "4",
            0.6: "6",
            0.5: "8",
            0.4: "a",
            0.3: "c",
            0.2: "e",
        }
        self.bottom_values = {
            0.9: "1",
            0.8: "3",
            0.7: "5",
            0.6: "7",
            0.5: "9",
            0.4: "b",
            0.3: "d",
            0.2: "f",
        }


    def get_lines(self, img):
        # Apply edge detection method on the image
        edges = cv2.Canny(img ,100, 200, apertureSize = 3)
        minLineLength = 10
        maxLineGap = 50
        # Use probabilistic high transform to find all the lines
        lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength, maxLineGap)
        return lines

    # Sort lines by horizontal position (left to right)
    def sort_lines(self):
        return sorted(self.lines, key=lambda lines: lines[0][0])

    def get_line_length(self, line):
        (x1,y1,x2,y2) = line[0]
        return np.abs(y1-y2)

    def lines_height_avg(self, lines):
        lines_height_total = 0
        for line in lines:
            lines_height_total += self.get_line_length(line)

        return lines_height_total / len(lines)

    def get_top_bottom_location(self, lines):
        top_total = 0
        bottom_total = 0
        for line in lines:
            for x1,y1,x2,y2 in line:
                top_total += y2
                bottom_total += y1

        top_avg = top_total / len(lines)
        bottom_avg = bottom_total / len(lines)
        return (top_avg, bottom_avg)

    def decode(self):
        hex_code = ""
        for i in range(2, len(self.lines), 2):
            lines = [self.lines[i], self.lines[i+1]]
            top, bottom = self.get_top_bottom_location(lines)
            top = np.abs(top - self.top)
            bottom = np.abs(bottom - self.bottom)

            height = self.lines_height_avg(lines)
            percentage =  height / self.max_length
            if top < bottom:
                key = min(self.top_values, key=lambda x:abs(x-percentage))
                hex_code += self.top_values[key]
            else:
                key = min(self.bottom_values, key=lambda x:abs(x-percentage))
                hex_code += self.bottom_values[key]

        return hex_code
