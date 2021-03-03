'''[Takes a picture]

This module is responsible for taking pictures in
a specific format.
'''
from picamera import PiCamera
from time import sleep
from sysVariable import IMGPATH


def takePicture(camera, path):
   """[Takes a picture and sends it to the specified path]

    The image MUST be of this size or it will not publish
    It depends on the data in the image, different images have
    different amounts of data.
   Args:
       camera ([a PiCamera object]): [controls the onboard camera
       and allowas for images to be taken]
       path ([system path]): [Designated location to save the image]
   """
   camera.resolution = (320,240)
   camera.capture(path, format='jpeg')


