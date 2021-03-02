''' Sets up the face collection service and initial admin


Accepts face collection name, users name, users phone number,
and users email. 

Requires the user to stand still for picture
'''
import click
import time
from initializeClient import faceCollectionSetup
from addUserKeys import addAdmin

@click.command()
@click.argument('faceCollectionName', type=click.STRING)
@click.argument('userName', type=click.STRING)
@click.argument('phoneNumber', type=click.STRING)
@click.argument('email', type=click.STRING)
def setup(faceCollectionName, userName, phoneNumber, email):
    # Call our faceCollection initializer
    print("Making face Collection... ")
    faceCollectionSetup(faceCollectionName)

    # Take our users picture and upload it with information
    print("Get ready for a picture!")
    time.sleep(3)
    addAdmin(userName, phoneNumber, email)