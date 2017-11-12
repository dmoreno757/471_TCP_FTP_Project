# Authors: Steve Sanchez, ???, ???
# Course: CPSC 471
# Due date: 11/16/17
# This program INSERT SOME DESCRIPTION
#

import socket
import os
import sys
import argparse
import time


# Print usage if user has incorrect number of arguments given and exit
if len(sys.argv) < 3:
    print("ERROR! Invalid # of arguments given. See sample input below:")
    print("python client.py" + " <server domain name> " + "<server port>")
    sys.exit(1)

# Store the arguments in variables
serv_name = sys.argv[1]
serv_port =int(sys.argv[2])

# Get and store the IP address of the domain name
serv_IP = socket.gethostbyname(serv_name)

ctrl_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ctrl_channel.connect((serv_IP, serv_port))

# This is just to make sure stuff is working right, DELETE AT END
print(serv_name, serv_port)
print(serv_IP)

# control channel is client to server connection for getting commands. Terminate at end/ quit command
# sooo, when server receives a quit command, server closes connection then client recognizes
# and closes as well.

# data channel is used for transferring data...generates new port for client and server 
# sooo, when user puts in a ls, get or put command, client creates ephemeral port for connection
# and then server connects to that new port for transfer to be done. Then that channel is closed
# Note: server has terminated NEW connection, NOT existing one for listening to client commands

while True:
    # Get input from the user
    line = raw_input("ftp> ")
    print(line)

    # Split the input into the command + arguments(if any)
    client_args = line.split()

    # First check if ls,get,or put commands to generate an ephemeral port for transfer 
    if (client_args[0] == 'ls' or client_args[0] == 'get' or client_args[0] == 'put'):
        # Create a socket used for data transfer
        data_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to port 0 and listen for response
        data_channel.bind(('',0))

        '''INSERT CODE FOR SENDING COMMANDS/DATA TO SERVER HERE'''
        
        data_channel.listen(1)
            while True:
                '''INSERT CODE FOR RETRIEVING DATA FROM SERVER HERE'''
                    '''Somehow detect its done sending in which case, break'''
                break
        data_channel.close()
    else:
        # Send client input to server
        '''INSERT CODE FOR SENDING COMMANDS/DATA TO SERVER HERE'''

        # If command is quit, prepare to close connection
        if (client_args[0] == 'quit'):
            # Prepare to close connection
            break
    
time.sleep(4.5)
# End client
ctrl_channel.close()
