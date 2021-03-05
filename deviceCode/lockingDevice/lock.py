from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from initializeClient import makeClient
import click
import RPi.GPIO as GPIO
import time 

pinName = 18
subTopic = 'Unlock'

# Set up GPIO for the lock
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinName, GPIO.OUT)
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

# Main function to be run on the lock device.
# It creates an MQTT client and subs to a topic
# that receives messages when a key is found. 
def runLock():

    # Make the client with out make client file
    client = makeClient()

    # Subscribe to the topic, go to faceWasKey method if
    # a message is received
    client.subscribe(subTopic, 1, faceWasKey)

    # Loop forever
    while True:
        time.sleep(1)


runLock()