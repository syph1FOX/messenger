from PyQt5 import QtCore, QtWidgets, QtNetwork
from PySide6.QtCore import QObject
from PySide6.QtNetwork import QTcpSocket

from .receive_thread import ReceiveThread
from shared.signals import SignalAndSlotsABC


class Client(QObject):#сделать сигналы которые будет принимать сервер
    def __init__(self):
        self.host = 'localhost'
        self.port = 5555
        if(self.connect(self.host, self.port)):
            print("connected")
        
        self.messages = []
        self.signals = SignalAndSlotsABC()
        self.socket = QTcpSocket()
        self.socket.readyRead.connect()
        self.connection_thread = ReceiveThread(self.socket)
        self.connection_thread.signal.connect() #ф-ия обрабатывающая получения сигнала от сервера
        self.connection_thread.start()
        
    def SlotReadyRead():
        pass
    def connect(self, host, port):#тупо подключение к серверу
        try:
            self.socket.connectToHost(host,port)
            return True

        except:
            print("Connection error")
            return False
        
    def check_account(self, login, password):#отправить сигнал серверу чтобы сервер проверил на бд акк с данными логином и паролем
        pass
    def reg_account(self, login, password):#отправить сигнал серверу чтобы сервер создал на бд акк с данными логином и паролем
        pass
    def send_message(self, message):#отправка сообщения конкретному челику

        print("sent: " + message)
        try:
            self.tcp_client.send(message.encode())
        except Exception as e:
            error = "Unable to send message '{}'".format(str(e))
            print("[INFO]", error)