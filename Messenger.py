#Author: Kasey Kolyno
#Date: 2/19/2016
#TCP Messenger

import socket

def init_connection ():
	TCP_IP = '127.0.0.1'   #for testing purposes (0.0.0.0 for INET)
	TCP_PORT = 9999        #personal preferance 
	BUFFER = 256
	skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defines the skt variable as a IP/TCP port
	skt.connect((TCP_IP, TCP_PORT))							#binds to socket/IP

def send_msg(text):	#define a send_msg function
	s.send(text)