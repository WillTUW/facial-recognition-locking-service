from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from sysVariable import DEVICENAME, ROOTCAPATH, PRIVATEKEYPATH, CERTIFICATEPATH, HOST
import time


def makeClient():
    mqttClient = None
    mqttClient = AWSIoTMQTTClient(DEVICENAME)
    port = 8883
    mqttClient.configureEndpoint(HOST, port)
    mqttClient.configureCredentials(ROOTCAPATH, PRIVATEKEYPATH, CERTIFICATEPATH)
    mqttClient.connect()
    mqttClient.publish('cameraClientConnected', 'The camera device has been initialized', 1)
    return mqttClient


makeClient()