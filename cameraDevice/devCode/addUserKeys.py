'''
Take in user Images here. This is where we will add our own 
user keys. Think about adding spunk to this, a button? Maybe a QR
code? 
'''
from cameraController import takePicture
from sysVariable import NEWFACE
import time 
from time import sleep
from picamera import PiCamera
import click

@click.command()
@click.argument('name', type=click.STRING)
def addUser(name):
    camera = PiCamera()
    camera.start_preview()
    sleep(2)
    takePicture(camera, NEWFACE)

    # Add MQTT client information for connecting
    # TODO
    # Publish image to topic where new client lambda is sitting
    # lambda shall take the new user and upload into S3
    # lambda needs to add the face to the s3 collection for rek



