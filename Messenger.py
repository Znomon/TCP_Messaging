#Author: Kasey Kolyno
#Date: 2/19/2016
#TCP Messenger

import socket

class msg():
   def init_connection(self):
      TCP_IP = '127.0.0.1'   #for testing purposes (0.0.0.0 for INET)
      TCP_PORT = 9999        #personal preferance 
      self.skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defines the skt variable as a IP/TCP port
      self.skt.bind((TCP_IP, TCP_PORT))                            #binds to socket/IP
      self.skt.listen(1)                                           #listens on that port

   def send_msg(text):	#define a send_msg function
      self.skt.send(text)

   def rec_msg(self):
      BUFFER = 256
      conn, addr = self.skt.accept()
      data = conn.recv(BUFFER)
      print data

ping = msg()
ping.init_connection()
ping.rec_msg()
   
   
