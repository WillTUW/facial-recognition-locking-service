""" Checks if an image is a face key for a device.

If it is a face key, the device will publish to an IoT topic 
to unlock the device and send messages to our admin
"""
import json
import boto3
import base64
s3 = boto3.client('s3')
client = boto3.client('rekognition')
IoTClient = boto3.client('iot-data', region_name = 'us-west-2')


bucket = 'facestoragefordetection'


def checkFaceKey(event, context):
    """Checks if an image is a key user

    Args:
        event ([json]): contains the image,
        admin list, and device Id for processing
        if the image is a key
    """
    
    
    # Convert the image back to writeable object
    img = base64.b64decode(event['image'])

    # Get the collection ID
    collectionID = event['faceCollection']
    message = {}

    # Get local variables
    message['admin_list'] = event['admin_list']
    message["device_id"] = event["device_id"]
    
    # Create file name and put into S3 storage
    file = 'temp' + '.jpeg'
    s3.put_object(Bucket=bucket, Key=file, Body=img)
    
    # Check if the image is in fact a user key
    response=client.search_faces_by_image(CollectionId=collectionID,
                                Image={'S3Object':{'Bucket':bucket,'Name':file}},
                                FaceMatchThreshold=70,
                                MaxFaces=1)

    # If the user is a key and the similiarity is greater than 75 percent
    # We will allow them access to the device. If images were higher quality,
    # the number would be considerably lower. 
    faceMatches=response['FaceMatches']
    for match in faceMatches:
            if match['Similarity'] > 75:
                
                # publish to the doorUnlock policy for the SMS message and 
                # deadbolt device to unlock. 
                # QOS of 1 because we need this to go through
                IoTClient.publish(topic='doorUnlock', qos=1, payload=json.dumps(message))
    
    
    
