CameraDevice

The device that contains the camera for facial detection and recognition.
This module assumes that it is being installed on a raspberry pi with a 
pi camera. 

Installation

[1] Run the requirnments.txt using
    $ pip install -r requirements.txt

[2] In sysVariable.py edit the file paths according to 
    the instructions in the file. This will allow the program to store, 
    retrieve, and edit information that will allowd the program to run. 
    Additionally, you will also need to download the AWS certification
    files for your thing and add the paths into the sysVariable.py document.

[3] Complete lock device setup and Cloud setup before continuing.
    Once the other modules are set up, navigate to the directory 
    that contains setup.py and write your arguments. Be ready for a 
    picture! The command will initialize your faceCollection and 
    add you as an admin, allowing for notifications when the door is unlocked
    $ python3 cli.py setup ARGS[faceCollectionName, userName, phoneNumber, email]

[4] TO add a user navigate to the directory and run. Be ready for a picture
    $ python3 cli.py adduser [name]

[5] To add an admin navigate to the directroy and run. Be ready for a picture
    $ python3 cli.py addadmin [name] [phonenumber] [email]

[6] To run the program after setup, navigate to the directory and run
    $ python3 cli.py deviceclienton

[7] If you need help with cli.py just run
    $ python3 cli.py --help

Testing and Evaluaiton

In testing.py, there are several tests with documentation to run it. 
This file does require some editing of components due to the nature
of the kind of work done in the program (IE Takes a picture, so camera
needs to be commented out and file paths assigned for images)

The results of the test indicate if the device successfully connected
to the IoT core and will show a black box approach of the cloud functinoality
IE if the lockDevice is running, the commands will function and you will 
see the lock operate accordingly. 

Check the lambda cloud logs in cloudwatch by clicking on your lambda function, 
navigating to monitor, and view logs in CloudWatch. Click on the latest 
execution to see what is occruing. This will allow you to see execution
details such as performance information. 
