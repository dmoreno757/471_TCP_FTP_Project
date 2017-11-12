# Authors: Steve Sanchez, ???, ???
# Course: CPSC 471
# Due date: 11/16/17
# This program INSERT SOME DESCRIPTION
#

import socket
import time


# Port for control channel
ctrl_port = 1234

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

    print("Accepted connection from client: ", addr)
    # PSUEDOCODE
    # If client_command == 'ls' OR client_command == 'get' OR client_command == 'put'
    # then us this code
    '''# Create a socket
data_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to port ??? .... I THINK PORT NUMBER IS BEING PASSED BY CLIENT HERE SO ITS GIVEN
data_channel.bind(('',given_port))

# Retreive the ephemeral port number
print "I chose ephemeral port: ", data_channel.getsockname()[1]'''
    
    time.sleep(4.5)

    # Close server side of connection
    command_sock.close()
