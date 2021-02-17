'''
This is our device Client
'''
from picamera import PiCamera
from time import sleep
# from faceDetection import faceDetection
import cv2 as cv
import boto3
import os
import logging
import time
import argparse
import json
import os
from picamera import PiCamera
from time import sleep
from sysVariable import IMGPATH
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from cameraController import takePicture
from faceDetection import faceDetection



def deviceClientOn():
    camera = PiCamera()
    camera.start_preview()
    sleep(2)
    while True:
        takePicture(camera, IMGPATH)
        sleep(10)
        if faceDetection(IMGPATH): 
            # Transmit the image to our aws iot core
    









deviceClientOn()






    

    

