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
        _, thresh = cv2.threshold(gray, 254, 255, 0)

        # finding the contours
        cnts, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        # just finds the biggest box, doesn't cover all edge cases
        c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

        # make a box out of the biggest rectangle
        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        box = np.int0(box)

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

        # crop and return just the barcode
        box_img = self.image[y1:y2, x1:x2]

        return box_img


if __name__ == '__main__':
    img = cv2.imread("scanner_test_images/barcode_on_forest.png")
    scn = Scanner(img)
    barcode = scn.detect_barcode()

    cv2.imshow('barcode', barcode)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
