""" Adds a new user to the face collection

Lambda functiont that is activated via a rule when
the device is adding a new user. 
"""
import json
import boto3
import os
import base64

# Define our s3 client
s3 = boto3.client('s3')
# Define our rekognition cliet
client = boto3.client('rekognition')


# This would be defined in the database
collection = 'keyFacesDoor1'


def addUserToCollection(event, context):
    """Adds a user to the face collection

    Args:
        event ([json]): contains persons name
    """
    # Create our bucket
    bucket = 'facestoragefordetection'

    # Bring the image back to a jpeg writeable format
    img = base64.b64decode(event['image'])
    
    # Save the file name
    file = event['name'] + '.jpeg'

    # Put the file in S3
    s3.put_object(Bucket=bucket, Key=file, Body=img)
    
    # Put the face in our collection
    response=client.index_faces(CollectionId=collection,
                                Image={'S3Object':{'Bucket':bucket,'Name':file}},
                                ExternalImageId=file,
                                MaxFaces=1,
                                QualityFilter="AUTO",
                                DetectionAttributes=['ALL'])

    # Print out confirmations that it was successful
    # Taken from AWS docs
    print ('Results for ' + file) 	
    print('Faces indexed:')	

    # Look at the data for the face and create IDs					
    for faceRecord in response['FaceRecords']:
         print('  Face ID: ' + faceRecord['Face']['FaceId'])
         print('  Location: {}'.format(faceRecord['Face']['BoundingBox']))

    print('Faces not indexed:')
    for unindexedFace in response['UnindexedFaces']:
        print(' Location: {}'.format(unindexedFace['FaceDetail']['BoundingBox']))
        print(' Reasons:')
        for reason in unindexedFace['Reasons']:
            print('   ' + reason)
    
    
    
    
