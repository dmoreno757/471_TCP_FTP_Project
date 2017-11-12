# Authors: Steve Sanchez, ???, ???
# Course: CPSC 471
# Due date: 11/16/17
# This program INSERT SOME DESCRIPTION
#

import socket
import os
import sys
import subprocess
import time

# Print usage if user has incorrect number of arguments given and exit
if len(sys.argv) < 1:
    print("ERROR! Invalid # of arguments given. See sample input below:")
    print("python client.py" +  "<port number>")
    sys.exit(1)
    
# Port for control channel
ctrl_port = int(sys.argv[1])

# Bind and listen to port
ctrl_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ctrl_channel.bind(('', ctrl_port))
ctrl_channel.listen(1)

# control channel is client to server connection for getting commands. Terminate at end/ quit command
# sooo, when server receives a quit command, server closes connection then client recognizes
# and closes as well.

# data channel is used for transferring data...generates new port for client and server 
# sooo, when user puts in a ls, get or put command, client creates ephemeral port for connection
# and then server connects to that new port for transfer to be done. Then that channel is closed
# Note: server has terminated NEW connection, NOT existing one for listening to client commands

while True:
    print("Awaiting connections...")

    # Accept commands at this connection
    command_sock, command_addr = ctrl_channel.accept()

    print("Accepted connection from client: ", command_addr)
    
    ''' INSERT CODE TO RETRIEVE COMMANDS/DATA FROM CLIENT HERE'''
    
    # If the client input a command and argument, then determine if get or put
    if (len(client_args) == 2):
        if(client_args[0] == 'get'):
            # Connect to ephemeral port for data transfer
            data_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            data_channel.connect(('',0))
            
            print("get check works")
        elif(client_args[0] == 'put'):
            # Connect to ephemeral port for data transfer
            data_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            data_channel.connect(('',0))
            
            print("put check works")
        else:
            print("ERROR! Invalid input given.")
            print("Usage: get <filename> OR put <filename>")

    # Else if the client input only a command, then determine if ls or quit
    elif (len(client_args) == 1):
        if(client_args[0] == 'ls'):
            # Connect to ephemeral port for data transfer
            data_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            data_channel.connect(('',0))

            # Run ls-equivalent command for Windows
            if os.name == 'nt':
                subprocess.call('dir', shell=True) # SOMEHOW NEED TO STORE THIS IN A STRING TO PASS TO CLIENT
            # Else run ls -l for Linux
            elif os.name == 'posix':
                subprocess.call(['ls', '-l'], shell=True) # SOMEHOW NEED TO STORE THIS IN A STRING TO PASS TO CLIENT
        elif (client_args[0] == 'quit'):
            # Close server side of connection
            command_sock.close()
            break
        else:
            print("ERROR! Invalid input given.")
            print("Usage: ls OR quit")
            
time.sleep(4.5)
# End server
ctrl_channel.close()
