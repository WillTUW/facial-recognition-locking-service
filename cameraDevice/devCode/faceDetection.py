'''
Detects faces using OpenCV HARR cascade model.
'''

import cv2 as cv
from sysVariable import FACE_DETECTION_MODULE
face_cascade = cv.CascadeClassifier(FACE_DETECTION_MODULE)


def faceDetection(imgPath):
    img = cv.imread(imgPath)
    grayImg = gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayImg)
    if len(faces) > 0:
        return True
    else:
        return False

