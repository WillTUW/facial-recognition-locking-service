""" Initilizes a client and collection

makeClient  : creates and returns the MQTT client

setup       : creates a face collection. Only run once
"""
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from sysVariable import DEVICENAME, ROOTCAPATH, PRIVATEKEYPATH, CERTIFICATEPATH, HOST, FACE_COLLECTION_ID, COLLECTION_CREATED
import time
import click

def makeClient():
    """Creates a client for MQTT

    Clients are made here to reduce the amount of repeatable code
    Returns:
        [MQTT.client]: AWS MQTT Client 
    """
    mqttClient = None
    mqttClient = AWSIoTMQTTClient(DEVICENAME)
    port = 8883
    mqttClient.configureEndpoint(HOST, port)
    mqttClient.configureCredentials(ROOTCAPATH, PRIVATEKEYPATH, CERTIFICATEPATH)
    mqttClient.connect()
    mqttClient.publish('cameraClientConnected', 'The camera device has been initialized', 1)
    time.sleep(5)
    return mqttClient

# Should only be ran once per device ... 
def faceCollectionSetup(idForCollection=FACE_COLLECTION_ID):
    """Is ran a single time per lockable device.

    Args:
        idForCollection ([string], optional): String name for collection. Defaults to FACE_COLLECTION_ID.
    """
    client = makeClient()
    client.publish('createFaceCollection', idForCollection, 1)
    print("Face Collection Created With ID: " + idForCollection)
    client.disconnect()
    
