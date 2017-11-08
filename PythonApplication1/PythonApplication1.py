
import socket
import sys
import os 
serverName = ecs.fullerton.edu
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(serverName, serverPort)
fileName = raw_input("Please enter the files name ")
fileTransfer = open(fileName, "r")
