import os
import logging
import click

from devCode import addUserKeys
from cameraControl import cameraOn
from deviceThing import deviceClientOn

@click.group()
def cli():


def main():
    cli.add_command(addUserKeys)
    cli.add_command(cameraOn)
    cli.add_command(deviceClientOn)

if __name__ == "__main__":
    main()
