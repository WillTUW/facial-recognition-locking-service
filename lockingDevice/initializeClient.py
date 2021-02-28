""" Initilizes a client

makeClient  : creates and returns the MQTT client
"""
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from sysVariable import DEVICENAME, ROOTCAPATH, PRIVATEKEYPATH, CERTIFICATEPATH, HOST
import time

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
    
