import os
import logging
import click

from addUserKeys import addUser
from cameraController import cameraOn
from deviceThing import deviceClientOn

@click.group()
def cli():
    '''Face Lock Command Line Interface'''

# main
def run():
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    cli.add_command(addUser)
    cli.add_command(cameraOn)
    cli.add_command(deviceClientOn)

if __name__ == "__main__":
    run()
