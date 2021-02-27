'''Texts the admin(s) when the device is unlocked.

If the face is key, the admin will receive a message in the form of
Device and time opened. 
'''
import json
import boto3
from datetime import datetime

# Define the SNS client
sns = boto3.client('sns')

def textAdmin(event, context):
    """Sends text to admin VIA AWS SNS if face key

    Args:
        event ([json]): contains 

        Admin list, device id
    """
    
    # Grab the contents of the event

    # Admin list has their phone, name, email 
    admin_dic = event['admin_list']

    # Just the device ID being activated
    device_id = event['device_id']

    # Get the date and time
    theTime = datetime.now().time()
    formTime = theTime.strftime("%H:%M:%S")

    # Text all of the admins that the device was accessed by
    # iterating the admin list
    for msgDest in admin_dic:
        number = "1" + msgDest['phone_number']
        adminName = msgDest['admin_name']
        aEmail = msgDest['email']
        text = adminName + ', ' + device_id + ' was accessed at ' + str(formTime)
        print(text)
        print(number)

        # Publish to the phone numbers
        sns.publish(PhoneNumber = number, Message=text)
    
    
