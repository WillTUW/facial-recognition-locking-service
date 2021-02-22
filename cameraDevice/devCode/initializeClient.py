from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from sysVariable import DEVICENAME, ROOTCAPATH, PRIVATEKEYPATH, CERTIFICATEPATH, HOST, FACE_COLLECTION_ID, COLLECTION_CREATED
import time
import click


def makeClient():
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
@click.command()
def createFaceCollection():
    client = makeClient()
    client.publish('createFaceCollection', FACE_COLLECTION_ID, 1)
    print("Face Collection Created With ID: " + FACE_COLLECTION_ID)
    
