__author__ = 'taira'

import socket
import sys

from Pyside.QtCore import *
from Pyside.QtGui import *


class Client(QWidget):

    def __init__(self, port, host=socket.gethostname()):

        self.app = QApplication(sys.argv)
        self.type_label = QLabel("Type:", self)
        self.type_text_field = QLineEdit(self)
        self.send_button = QPushButton("Send", self)

        self.sock = socket.socket()
        self._host = str(host)
        self._port = port
        self.address = (self._host, self._port)

        self.message_to_send = None
        self.name = None

        self.win_height = 400
        self.win_width = 400


        self.initUI()

    def connect(self):
        self.sock.connect(self.address)

    def end(self):
        self.sock.close()
        sys.exit()

    def receive(self):
        self.sock.recv(1024).decode()

    def send(self):
        self.sock.send(self.message_to_send.encode())

    def communicate(self):
        self.connect()
        self.receive()
        self.name = input("Name: ")

        while True:
            message = input("me: ")

            if message.lower() == "q":
                break
            self.message_to_send = self.name + ": " + message
            self.send()

    def initUI(self):
        QWidget.__init__(self)
        self.setWindowTitle("chat client")
        self.setMinimumSize(self.win_width, self.win_height)

        self.type_text_field.setPlaceholderText("Type something...")

        self.show()
        self.app.exec_()


client = Client(port=5000)
client.connect()
client.receive()
client.communicate()
client.end()