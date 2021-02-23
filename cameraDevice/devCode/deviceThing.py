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
import click
import base64
from picamera import PiCamera
from time import sleep
from sysVariable import IMGPATH
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from cameraController import takePicture
from faceDetection import faceDetection
from initializeClient import makeClient

topic = 'faceToCompare'
@click.command()
def deviceClientOn():
    client = makeClient()
    camera = PiCamera()
    camera.start_preview()
    sleep(2)
    while True:
        # takePicture(camera, IMGPATH)
        # sleep(10)
        if faceDetection(IMGPATH):
            # Transmit the image to our aws iot core
            print('face detected... sending to cloud')
            with open(IMGPATH, 'rb') as file:
                img = file.read()

            # We need to encode the image to be in a byte format for MQTT
            data = base64.b64encode(img)
            # Send to cloud
            client.publish(topic, json.dumps(data.decode('utf-8')), 1)
            



        sleep(10)
