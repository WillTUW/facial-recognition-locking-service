'''
Take in user Images here. This is where we will add our own 
user keys. Think about adding spunk to this, a button? Maybe a QR
code? 
'''
import json
import base64
from cameraController import takePicture
from sysVariable import NEWFACE
import time 
from time import sleep
from picamera import PiCamera
import click
from faceDetection import faceDetection
from initializeClient import makeClient
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from PIL import Image


topic = 'addUser'
@click.command()
@click.argument('name', type=click.STRING)
def addUser(name):

    # Create the camera object
    camera = PiCamera()
    camera.start_preview()
    sleep(2)


    # takePicture(camera, NEWFACE)

    # If there is a face then
    # send message to iot for processing and storign
    # inside of the Collection
    if faceDetection(NEWFACE):
        client = makeClient()
        #data = {}
        with open(NEWFACE, 'rb') as file:
            img = file.read()

        # We need to encode the image to be in a byte format for MQTT
        data = base64.b64encode(img)
        # Send to cloud
        message = {
            "name": name,
            "device ID": "Door1",
            "image": data.decode('utf-8') 
        }

        client.publish(topic, json.dumps(message), 1)
        # client.publish(topic, json.dumps(data.decode('utf-8')), 1)

    else:
        print("No face found :(")
        



