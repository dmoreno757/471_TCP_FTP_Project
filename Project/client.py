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
serv_port = sys.argv[2]

# Get and store the IP address of the domain name
serv_IP = socket.gethostbyname(serv_name)

ctrl_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ctrl_channel.connect((serv_IP, int(serv_port)))

# This is just to make sure stuff is working right, DELETE AT END
print(serv_name + " " + serv_port)
print(serv_IP)

# control channel is client to server connection for getting commands. Terminate at end/ quit command
# sooo, when server receives a quit command, server closes connection then client recognizes
# and closes as well.

# data channel is used for transferring data...generates new port for client and server 
# sooo, when user puts in a ls, get or put command, client creates ephemeral port for connection
# and then server connects to that new port for transfer to be done. Then that channel is closed
# Note: server has terminated NEW connection, NOT existing one for listening to client commands

while True:
    
    # FIGURE OUT HOW TO GET SEPARATE ARGUMENTS FROM USER, MAKE SURE ITS VALID, AND SEND

    #command = str(input("ftp>
    # if command == 'ls -l':
    '''
import subprocess

# Run ls command, get output, and print it
subprocess.call('dir', shell=True)

#if we can somehow detect linux system, do this command
#subprocess.call(['ls', '-l'], shell=True)'''
    
# PSUEDOCODE
#   If command == 'quit':
#                         break

# ctrl_channel.close()

time.sleep(4.5)
