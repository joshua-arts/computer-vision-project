import cv2 
import numpy as np 
import imutils

class Scanner:
    def __init__(self, image):
        self.image = image


    def detect_barcode(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        ret, gray = cv2.threshold(gray, 254, 255, 0)

        mask = np.zeros(gray.shape, np.uint8)

        cnts, hier = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(self.image, [box.astype(int)], -1, (0, 255, 0), 3)

        cv2.imshow('box', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    img = cv2.imread("scanner_test_images/barcode_on_car.png")
    scn = Scanner(img)
    scn.detect_barcode()

