"""[Command Line Interface for Face Lock]
Uses click to create a CLI. The CLI allows 
the user to input whaterver parameters and start
the program. Ideally, there would be a UI here, 
but I don't have a lot of experience with that.
"""
import os
import logging
import click

from addUserKeys import addUser, addAdmin
from cameraController import takePicture
from deviceThing import deviceClientOn
from initializeClient import setup
from sysVariable import COLLECTION_CREATED

@click.group()
def cli():
    '''Face Lock Command Line Interface'''


def main():
    """[No inputs required, this is the main. It acts as the 
    driver for the whole program. Using click, we can load 
    commands that will do certain things in the program]
    """
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # Add user command accepts a name as input
    cli.add_command(addUser)


    # addAdmin comman accepts name, phonenumber, and email
    # as input
    cli.add_command(addAdmin)


    # Starts the client program
    cli.add_command(deviceClientOn)


    # Only meant to be ran once, it is the setup for the 
    # rekognition services. Accepts a string that 
    # represents the id for collection face
    cli.add_command(setup)


    cli()

if __name__ == "__main__":
    main()
