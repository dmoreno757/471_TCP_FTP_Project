# Authors: Steve Sanchez, ???, ???
# Course: CPSC 471
# Due date: 11/18/17
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

def sendData(args, conn_channel):
    # Get the size of the data read and convert it to string
    dataSizeStr = str(len(args))
    print(dataSizeStr)
    print(len(args))
    
    # Prepend 0's to the size string until the size is 10 bytes
    while len(dataSizeStr) < 10:
         dataSizeStr = "0" + dataSizeStr
         
    # Prepend the size of the data to the file data.
    args = dataSizeStr + args

    # The number of bytes sent
    numSent = 0
    
    # Send the data!
    while len(args) > numSent:
        numSent += conn_channel.send(args[numSent:])

def sendFile(args):
    # Read file data
    fileObj = open(args[1], "r")
    fileData = fileObj.read()
        
    # Make sure we did not hit EOF
    if fileData:
        sendData(fileData)
'''
# ************************************************
# Receives the specified number of bytes
# from the specified socket
# @param sock - the socket from which to receive
# @param numBytes - the number of bytes to receive
# @return - the bytes received
# *************************************************
def recvAll(sock, numBytes):

	# The buffer
	recvBuff = ""
	
	# The temporary buffer
	tmpBuff = ""
	
	# Keep receiving till all is received
	while len(recvBuff) < numBytes:
		
		# Attempt to receive bytes
		tmpBuff =  sock.recv(numBytes)
		
		# The other side has closed the socket
		if not tmpBuff:
			break
		
		# Add the received bytes to the buffer
		recvBuff += tmpBuff
	
	return recvBuff
    
def receiveData(command_sock):
	# The buffer to all data received from the the client.
	fileData = ""
	
	# The temporary buffer to store the received data.
	recvBuff = ""
	
	# The size of the incoming file
	fileSize = 0	
	
	# The buffer containing the file size
	fileSizeBuff = ""
	
	# Receive the first 10 bytes indicating the size of the file
	fileSizeBuff = recvAll(command_sock, 10)
	
	# Get the file size
	fileSize = int(fileSizeBuff)

	print ("The file size is ", fileSize)
	
	# Get the file data
	fileData = recvAll(command_sock, fileSize)
	
	print ("The file data is: ")
	print (fileData)

	return fileData
 '''

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

        # Send commands over control channel
        sendData(client_args[0], ctrl_channel)
        
        data_channel.listen(2)
        while 2:
            print("Established data channel connection")
            
        data_channel.close()
        
    else:
        # Send commands over control channel
        sendData(client_args[0], ctrl_channel)

        # If command is quit, prepare to close connection
        if (client_args[0] == 'quit'):
            # Prepare to close connection
            break

# End client
ctrl_channel.close()
