"""Adds users and admins to the face collection

addUser: Accepts a users name as an input parameter. It
will take a picture of the user and if successful, will
send the image to AWS IoT lambda that will add it to
the collectiona and store in S3. Once sent via MQTT
the user name is written into a JSON file that houses
all the users names. Ideally, this would be a MySQL
server hosted on AWS and passed in via MQTT, but 
that is a paid service and is a bit outside of the 
scope of my project. In an ideal world, we the backend
would have better storing methods. 

addAdmin: Much like the addUser method, this accepts
an admin name, email, and phonenumber. The method
will activate the camera and take a picture, if
successful, it send the message to an AWS lambda function
as previously defined. The admin will also be stored locally
in a JSON file

"""
import json
import base64
from cameraController import takePicture
from sysVariable import NEWFACE, PATH_TO_USERS
import time 
from time import sleep
from picamera import PiCamera
import click
from faceDetection import faceDetection
from initializeClient import makeClient
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from PIL import Image


topic = 'addUser'

"""Add user puts  a new key into the face collection

The method accepts a name as an argument. The name should be
used to identify the user. A camera object is created to 
take a picture of the new user. A three second count will
be given to prepare the user for the picture. If the users
face is unclear in the picture, they will be forced
to run the addUser again and pose again for a picture. If
the face is accepted, the users face will be converted
into a byte representation of an image, sent to utf-8,
and published via MQTT. Once published, the users name 
will be stored locally in a JSON file. Ideally, we would
use MySQL and store it in AWS, but that is paid and a 
bit out of scope for what I am doing in this project.
Once execution is completed, code will complete and
resources dismissed. 
"""
@click.command()
@click.argument('name', type=click.STRING)
def addUser(name):

    # Create the camera object
    camera = PiCamera()
    camera.start_preview()
    sleep(2)

    # Give a 3 second count 
    for x in range(3):
        print(x + 1)
        sleep(1)
    takePicture(camera, NEWFACE)

    # If there is a face then
    # send message to iot for processing and storign
    # inside of the Collection
    if faceDetection(NEWFACE):
        client = makeClient()
        with open(NEWFACE, 'rb') as file:
            img = file.read()

        # We need to encode the image to be in a byte format for MQTT
        data = base64.b64encode(img)
        # Send to cloud
        message = {
            "name": name,
            "device ID": "Door1",
            "image": data.decode('utf-8') 
        }
        client.publish(topic, json.dumps(message), 1)
        
        # Write the user to file
        with open(PATH_TO_USERS) as userList:
            users = json.load(userList)

            base_user = users['users']
            newUser = {"name": name}
            base_user.append(newUser)

        with open(PATH_TO_USERS, 'w') as writefile:
            json.dump(users, writefile, indent=4)

        # Disconnect the client
        client.disconnect()

    else:
        print("No face found :(")



"""Add admin puts a new admin key into the face collection

The method accepts a name, phonenumber, and email as
arguments. The name should be used to identify the admin.
The phonenumber should be the number they wish to 
recieve messages when the door is unlocked, and 
the email should be where the logs maybe get dumped.  
A camera object is created to take a picture of the new user.
A three second count will be given to prepare the user for 
the picture. If the usersface is unclear in the picture, 
they will be forcedto run the addUser again and pose again 
for a picture. Ifthe face is accepted, the users face 
will be convertedinto a byte representation of an image, 
sent to utf-8, and published via MQTT. Once published, 
the admins name, number, and email will be stored locally 
in a JSON file. Ideally, we woulduse MySQL and store it
in AWS, but that is paid and a bit out of scope for what 
I am doing in this project.Once execution is completed, 
code will complete and resources dismissed. 
"""
@click.command()
@click.argument('name', type=click.STRING)
@click.argument('phonenumber', type=click.STRING)
@click.argument('email', type=click.STRING)
def addAdmin(name, phonenumber, email):
    camera = PiCamera()
    camera.start_preview()
    sleep(2)
    # Give a 3 second count 
    for x in range(3):
        print(x + 1)
        sleep(1)
    
    # Take pcitrue of the user
    takePicture(camera, NEWFACE)

    # If the image is clear and the face detected
    if(faceDetection(NEWFACE)):
        print('Face was found')

        # Make our MQTT client
        client = makeClient()

        # Open the image we took
        with open(NEWFACE, 'rb') as file:
            img = file.read()

        # Convert it to base64
        data = base64.b64encode(img)

        # Write our message that is intended
        # for a lambda to use
        message = {
            "name": name,
            "device ID": "Door1",
            "image": data.decode('utf-8') 
        }
        
        # Dump the message and publish to topic
        client.publish(topic, json.dumps(message), 1)

        # Open up our local JSON storage
        with open(PATH_TO_USERS) as userList:
            users = json.load(userList)

            # Get the dictionary that we want
            admins = users['admin_list']
            newAdmin = {"admin_name": name, 
                        "email": email, 
                        "phone_number": phonenumber
                        }

            # Append the message to the file
            admins.append(newAdmin)

        # Write the file
        with open(PATH_TO_USERS, 'w') as writefile:
            json.dump(users, writefile, indent=4)

    # This is the case that no face was found and it is 
    # time to try again 
    else:
        print("No Face Found, try again!")
        print("exiting... ")
