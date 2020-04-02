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

        #draw the box over the original image
        cv2.drawContours(self.image, [box.astype(int)], -1, (0, 255, 0), 3)

        cv2.imshow('box', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # cv2.imwrite("detected_barcode.png", self.image)

        # TODO: cut out the box and return just the barcode

        return self.image


if __name__ == '__main__':
    img = cv2.imread("scanner_test_images/barcode_on_forest.png")
    scn = Scanner(img)
    scn.detect_barcode()

