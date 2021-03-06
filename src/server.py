__author__ = 'taira'

import socket
import threading


def client_thread(connection):
    connection.send("Thank you for connecting".encode())
    while True:
        data = connection.recv(1024).decode()
        if not data or data.lower().split()[1] == "q":
            break
        print(data)
    connection.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = socket.gethostname()
port = 5000

s.bind((host, port))

s.listen(5)

while True:
    connection, address = s.accept()
    print("connection from " + address[0])

    threading._start_new_thread(client_thread, (connection,))

s.close()

