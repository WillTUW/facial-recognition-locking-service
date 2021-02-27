""" Creates a face collection for rekognition

Function called once during setup and will have a collection ID 
"""
import json
import boto3
client = boto3.client('rekognition')
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)
# This function creates a face collection for each lockable device
#  there is on the network
def createFaceCollection(event, context):
    """Create face collection

    Args:
        event ([json]): [contains the collection id]
    """
    # ID is passed in from the device
    id = event['collection']
    message = {"collection" : id}
    
    
    # Create a collection and save as response to print back confirmations 
    # if the creation fails, that is an indicator that it has already been
    # created for this device. 
    try:
        response = client.create_collection(CollectionId=id)
        # Print our confirmations]
        print('Collection made with name ' + id)
        print('Collection has been created...')
        print('Collection ARN: ' + response['CollectionArn'])
    except ClientError:
        logger.exception("Can't create the collection, it may have already been made")
        raise
    
    
    
