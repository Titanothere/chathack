__author__ = 'taira'

import socket
import sys

s = socket.socket()

host = socket.gethostname()
port = 5000

s.connect((host, port))
print(s.recv(1024).decode()) #what does the number mean?
name = input("name: ")
while True:
    message = input("me: ")
    message_to_send = name + ": " + message
    s.send(message_to_send.encode())
    if message.lower() == "q":
        break
s.close()
sys.exit()