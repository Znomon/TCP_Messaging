#Author: Kasey Kolyno
#Date: 2/19/2016
#TCP Messenger

import socket

TCP_PORT = '127.0.0.1' #for testing purposes
TCP_PORT = 9999        #personal preferance 

BUFFER = 2048

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defines the skt variable as a IP/TCP port
skt.connect((TCP_IP, TCP_PORT))							#binds to socket/IP
