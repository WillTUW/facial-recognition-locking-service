'''
Detect faces using MTCNN or openCV
'''


import cv2 as ocv
from mtcnn.mtcnn import MTCNN
from matplotlib import pyplot as plt

face_detection = MTCNN()

def faceDetection(image, imgPath):
    '''
    if there is a face:
        return true
    else
        return false
    '''
    '''
    faceCascade = cv2.CAscadeClassifier(PATH_TO_OCV)
    # Set to grayscale
    gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Get number of faces from the model (this will be sufficient for determining the faces)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    if(faces > 0):
        return true
    
    else:
        return false
    '''
    # Maybe pass in as imgPath :) eliminate the path variable
    imagePlt = plt.imread(imgPath)
    faces = face_detection.detect_faces(image)
    if faces > 0:
        return True
    else:
        return False