''' Basic unit tests / unit tests that will show the basic 
functionality of the program. 

This testing file assumes that a collection has already been defined. IE 
this program has been initialized via CLI.py

NOTE: Check cloud logs to see the outputs :)
'''

from sysVariable import IMGPATH, FACE_COLLECTION_ID, DEVICENAME, PATH_TO_USERS
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from cameraController import takePicture
from faceDetection import faceDetection
from initializeClient import makeClient
from addUserKeys import addUser, addAdmin
from deviceThing import deviceClientOn

def clientTest():

    print('Testing the client...')
    # Check the AWS console for a message from device.
    # On creation, there message is published to a testing
    # Topic.
    client = makeClient()

# Pass in a face image path to the face detection
# Module, if it returns true, it worked
def faceDetectionTest():
    print('Testing face detection...')

    # Real Face
    facePath = ''
    assert faceDetection(facePath) != 1, 'The face was not detected'

    # No face
    noFacePath = ''
    assert(faceDetection(noFacePath)) != 0, 'Failed no face detected, but detected'

# This section is a bit more complex to test and will require slight modification to the
# addUser method in addUserKeys. If you desire to not pose for the tests, comment out line
# 68 (camera taking picture), and NEWFACE needs a new path with a face image of size 320 x 240
# Testing phone number and email must be set up for the messaging. 
# You can only do one at a time. You will need to update the image from the user when testing admin. 
# If a user is also an admin that could be a bit weird. 
def addUsersTest():
    print('Testing add users...')

    # Add a base user
    addUser('TestUser')

    # Add an admin user
    # addAdmin('TestAdmin', 'YOURPHONENUMBER', 'YOUREMAIL')


# To test this file you will need to reassign the IMGPATH to an image with the 
# face in question. Comment out the camera as well. 
def deviceThingTest():
    print('Testing the device functionality...')

    # Test with a real key user by assigning the correct path.
    # OR test with a non key face by assigning the IMGPATH
    deviceClientOn()



clientTest()
faceDetectionTest()
addUsersTest()
deviceThingTest()