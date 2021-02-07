'''
Testing camera file, make sure it is functioning
'''
from picamera import PiCamera
from time import sleep
from sysVariable import IMGPATH

def CameraOn():
   camera = PiCamera()
   camera.start_preview()

   camera.capture(IMGPATH)