'''[Takes a picture]

This module is responsible for taking pictures in
a specific format.
'''
from picamera import PiCamera
from time import sleep
from sysVariable import IMGPATH


def takePicture(camera, path):
   """[Takes a picture and sends it to the specified path]

   Args:
       camera ([a PiCamera object]): [controls the onboard camera
       and allowas for images to be taken]
       path ([system path]): [Designated location to save the image]
   """
   camera.resolution = (1024,768)
   camera.capture(IMGPATH, format='jpeg')


