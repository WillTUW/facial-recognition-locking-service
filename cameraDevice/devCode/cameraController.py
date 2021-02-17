'''
Testing camera file, make sure it is functioning
'''
from picamera import PiCamera
from time import sleep
from sysVariable import IMGPATH


# Accepts a camera device and path to store image
def takePicture(camera, path):
   camera.resolution = (1024,768)
   camera.capture(IMGPATH, format='jpeg')


