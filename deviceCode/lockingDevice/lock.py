from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from initializeClient import makeClient
import click
import RPi.GPIO as GPIO
import time 

pinName = 18
subTopic = 'Unlock'
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setuprelay(GPIO.OUT)
GPIO.output(pinName, 0)


def faceWasKey(client, arg, arg2):
    """callback for messages to unlock

    Args:
        client ([MQTT]): client
    """
    print('Was A Key... Unlockng')

    # Set lock state to open
    GPIO.output(pinName, 1)

    # Sleep for 30
    time.sleep(30)

    # Set lock state to lock
    GPIO.output(pinName, 0)

    print('Device Locked')


def runLock():
    client = makeClient()

    client.subscribe(subTopic, 1, faceWasKey)
    while True:
        time.sleep(1)

