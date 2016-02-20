#Author: Kasey Kolyno
#Date: 2/19/2016
#TCP Messenger

import socket
from tkinter import *

def sendTxt(event):
   print ("nothing")

class msg():
   #Handles Message communication
   def init_connection(self):
      TCP_IP = '127.0.0.1'   #for testing purposes (0.0.0.0 for INET)
      TCP_PORT = 9999        #personal preferance 
      self.skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defines the skt variable as a IP/TCP port
      self.skt.bind((TCP_IP, TCP_PORT))                            #binds to socket/IP
      self.skt.listen(1)                                           #listens on that port

   def send_msg(self, text):	#define a send_msg function
      #self.skt.send(text)
      print ("nothing")

   def rec_msg(self):
      BUFFER = 256
      conn, addr = self.skt.accept()
      data = conn.recv(BUFFER)
      print (data)

class createWindow():
   #handles the user interface
   window = Tk()
   window.title("TCP MESSENGER")

   ping = msg()
   ping.init_connection()

   topFrame = Frame(window)
   bottomFrame = Frame(window)

   topFrame.pack()
   bottomFrame.pack(side=BOTTOM)
   
   message = Entry(topFrame)
   message.pack(side=LEFT)
   submit = Button(topFrame, text = "Send") #command = ping.send_msg(message.get()))
   submit.bind("<Submit>", sendTxt)
   submit.pack(side=RIGHT)
   text = Text(bottomFrame, width = 35, height = 5, wrap = WORD)
   text.pack()

   window.mainloop()
   


window = createWindow()


   #ping = msg()
   #ping.init_connection()
   
   
