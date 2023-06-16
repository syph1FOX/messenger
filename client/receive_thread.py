from PyQt5 import QtCore, QtWidgets
from PySide6.QtNetwork import QTcpSocket

class ReceiveThread(QtCore.QThread):#поток принятия инфы от сервера. Здесь надо сделать сигналы ответа сервера и их обработку
    signal = QtCore.pyqtSignal(str)

    def __init__(self, client_socket:QTcpSocket):
        super(ReceiveThread, self).__init__()
        self.client_socket = client_socket

    def run(self):
        while True:
            self.receive_message()

    def receive_message(self):
        #message = self.client_socket.recv(1024)
        message = message.decode()

        print(message)
        self.signal.emit(message)
        return message