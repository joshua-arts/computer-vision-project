import cv2 
import numpy as np 
import imutils

class Scanner:
    def __init__(self, image):
        self.image = image


    def detect_barcode(self):
        # grayscale image
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        # geting the threshold image
        _, thresh = cv2.threshold(gray, 230, 255, 0)

        # finding the contours
        cnts, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        # just finds the biggest box, doesn't cover all edge cases
        c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

        # make a box out of the biggest rectangle
        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        # cv2.drawContours(self.image, [box.astype(int)], -1, (0, 255, 0), 3)

        # cv2.imshow('box', self.image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        x1 = self.image.shape[1]
        x2 = 0
        y1 = self.image.shape[0]
        y2 = 0

        # get the box points
        for point in box:
            if point[0] < x1: x1 = point[0]
            if point[0] > x2: x2 = point[0]
            if point[1] < y1: y1 = point[1]
            if point[1] > y2: y2 = point[1]

        x_off = (x2-x1)*0.025
        y_off = (y2-y1)*0.025

        x1 = int(x1 + x_off)
        x2 = int(x2 - x_off)
        y1 = int(y1 + y_off)
        y2 = int(y2 - y_off)

        # crop and return just the barcode
        box_img = self.image[y1:y2, x1:x2]
        box_img = cv2.cvtColor(box_img, cv2.COLOR_BGR2GRAY)
        _, box_thresh = cv2.threshold(box_img, 127, 255, 0)

        blurred = cv2.GaussianBlur(box_thresh, (3, 3), cv2.BORDER_DEFAULT)
        _, box_thresh = cv2.threshold(blurred, 200, 255, 0)

        return box_thresh


if __name__ == '__main__':
    img = cv2.imread("camera_img.png")
    scn = Scanner(img)
    barcode = scn.detect_barcode()

    cv2.imshow('barcode', barcode)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
