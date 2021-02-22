import os
import logging
import click

from addUserKeys import addUser
from cameraController import takePicture
from deviceThing import deviceClientOn
from initializeClient import createFaceCollection
from sysVariable import COLLECTION_CREATED

@click.group()
def cli():
    '''Face Lock Command Line Interface'''


# main
def main():
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    cli.add_command(addUser)
    cli.add_command(deviceClientOn)
    cli.add_command(createFaceCollection)
    cli()

if __name__ == "__main__":
    main()
