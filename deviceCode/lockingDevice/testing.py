''' Basic unit tests / unit tests that will show the basic 
functionality of the program. 

This testing file assumes that a collection has already been defined. IE 
this program has been initialized via CLI.py

'''
from initializeClient import makeClient
from lock import faceWasKey
def clientTest():

    print('Testing the client...')
    # Check the AWS console for a message from device.
    # On creation, there message is published to a testing
    # Topic.
    client = makeClient()

# The following functino simulates the MQTT message to the lock device 
# Telling it that it is time to open the lock. If the lock visibly moves,
# it worked
def lockTest():
    print('Testing the lock! Watch and see if it opens')

    # Call the function that is to be run on the device
    faceWasKey()


clientTest()
lockTest()