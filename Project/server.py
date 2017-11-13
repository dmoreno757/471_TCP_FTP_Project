# Authors: Steve Sanchez, ???, ???
# Course: CPSC 471
# Due date: 11/18/17
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


'''def sendData(args, conn_channel):
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

while True:
    print("Awaiting connections...")

    # Accept commands at this connection
    command_sock, command_addr = ctrl_channel.accept()

    print("Accepted connection from client: ", command_addr)
    
    command = receiveData(command_sock)
    print("command is", command)
    
    # If command is ls, get, or put, then connect to ephemeral port for data transfer
    if (command == 'ls' or command == 'get' or command == 'put'):
        data_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        data_channel.connect(('0.0.0.0',0))


        # If the command is get, send over the file requested
        if (command == 'get'):
            print("get check works")

        # Else if the command is put, retrieve the file from the client and store
        elif(command == 'put'):
            print("put check works")

        # Else the command is ls so display items in directory
        else:
            # Run ls-equivalent command for Windows
            if os.name == 'nt':
                subprocess.call('dir', shell=True) # SOMEHOW NEED TO STORE THIS IN A STRING TO PASS TO CLIENT

            # Else run ls -l for Linux
            elif os.name == 'posix':
                subprocess.call(['ls', '-l'], shell=True) # SOMEHOW NEED TO STORE THIS IN A STRING TO PASS TO CLIENT

        # Close the data channel connection
        data_channel.close()
        
    # Else if the command is quit, prepare to close connection
    elif (command == 'quit'):
        # Close server side of connection
        command_sock.close()
        break
    
    # Else the command is not recognized so print error message
    else:
        print("FAILURE. Invalid input given.")
        print("Usage: get <filename> OR put <filename>")
        print("Usage: ls OR quit")
          
# End server
ctrl_channel.close()
