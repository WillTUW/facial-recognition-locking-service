""" deviceThing is our device functionality

It continously takes images looking for keys to unlock the device.
If a key is found via Face Detection, it will be published
VIA MQTT to IoT Topic for Facial Recognition in AWS. 

Note: 

Instead of storing users in JSON, I would rather store in 
a MySQL database. The cost and integration of such database
is too high and out of scope for the project. But, if 
this were a real product there would be numerous databases
for better storage practices. 

"""
from picamera import PiCamera
from time import sleep
# from faceDetection import faceDetection
import cv2 as cv
import boto3
import logging
import time
import argparse
import json
import os
import click
import base64
from time import sleep
from sysVariable import IMGPATH, FACE_COLLECTION_ID, DEVICENAME, PATH_TO_USERS
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from cameraController import takePicture
from faceDetection import faceDetection
from initializeClient import makeClient

topic = 'faceToCompare'
waitTopic = 'deviceMustWait'
doorUnlockedTopic = 'doorUnlock'



def waitInit(client, userdata, command):
    """Sends Message to AWS IoT

    Args:
        client ([MQTT Client]): [connection to IoT core]
        userdata ([type]): [description]
        command ([type]): [description]

    Ideally, this method would be used by creating multiple client
    connections, but my device kept timing out (I think do to resourcing
    issues). This function would take place of the combined image write 
    and would send the admin contacts via this channel
    """
    print('User was accepted')

    with open(PATH_TO_USERS) as file:
        readData = json.load(file)
    
    message = {
        "device_id" : DEVICENAME, "admin_list" : []
    }
    message['admin_list'] = readData['admin_list']
    client.publish(doorUnlockedTopic, json.dumps(message), 1)


@click.command()
def deviceClientOn():
    """Turns on the camera and searches for users

    This function is continous. It takes images and 
    sends them through facial recognition. If there is a face
    found, the device will publish it to the cloud. Once in the
    cloud it will determine if there is  to be a wait or not 
    (If face, then wait). But, I am applying a wait regardless 
    to mitigate the cost of the project on the backend. 
    """

    # Make the client
    client = makeClient()
    camera = PiCamera()
    camera.start_preview()
    sleep(2)

    # Continous looping for user images. If there is a face
    # The loop will pause and the user key will be evaluated.
    while True:

        # Take a piture and save it to a specific path
        takePicture(camera, IMGPATH)

        # If face detected it will send to AWS IoT Core
        if faceDetection(IMGPATH):

            print('face detected... sending to cloud')

            # Open the newly aquired face
            with open(IMGPATH, 'rb') as file:
                img = file.read()

            # open users for admin messages.
            # Ideally this would be in an MySQL server, but 
            # that is a paid service in AWS and time consuming
            with open(PATH_TO_USERS) as users:
                readData = json.load(users)
            
            # We need to encode the image to be in a byte format for MQTT
            data = base64.b64encode(img)

            # Create our dictionary to send the data in
            message = {
                "image" : data.decode('utf-8'),
                "faceCollection" : FACE_COLLECTION_ID,
                "admin_list" : readData['admin_list'],
                "device_id" : DEVICENAME
            }

            # Send to cloud
            client.publish(topic, json.dumps(message), 1)

            # Buffer for processing time
            # Sleep for 30 seconds as camera cooldown / as to not spam
            # the AWS service ($$$)
            print('Waiting...')
            sleep(30)
        else: 
            # No face was detected, we sleep only for 10 seconds
            print("No face found... Looking again in 10 seconds")
            sleep(10)
    
