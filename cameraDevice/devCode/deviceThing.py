'''
This is our device Client
'''
from picamera import PiCamera
from time import sleep
from faceDetection import faceDetection
import mtcnn
import boto3
import os


def deviceClientOn():
    # This client will talk with rekoginition and check if the face 
    # is a key to the lock
    imageClient = boto3.client('rekognition')

    

    

