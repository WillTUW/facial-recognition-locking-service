"""Detects faces using the HARR cascade classifier

Using OpenCV we are able to detect if there are faces
in the image. The CascadeClassifier is pretrained model
that will convolve kernels to determine any facial features.
It can detect multiple faces in an image but will not 
conduct facial recognition. If the input parameter is 
a face, the method will reply true. 
"""

import cv2 as cv
from sysVariable import FACE_DETECTION_MODULE
face_cascade = cv.CascadeClassifier(FACE_DETECTION_MODULE)


def faceDetection(imgPath):
    """Detects faces that are within an image

    Args:
        imgPath ([file]): [a path to an image that
        was taken recently]

    Returns:
        [boolean]: [if there is a face detected
        the result will be true,
        if not, the result false.]
    """

    # Read the image from the local path
    img = cv.imread(imgPath)

    # Convert the image to gscale
    grayImg = gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Apply the model to the image
    faces = face_cascade.detectMultiScale(grayImg)

    # We only care if there is an image in the picture.
    # If there is no image, the result would be 0
    if len(faces) > 0:
        return True
    else:
        return False

        