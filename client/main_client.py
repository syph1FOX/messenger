from PyQt5 import QtCore, QtWidgets, QtNetwork
from PySide6.QtCore import QObject, QDataStream
from PySide6.QtNetwork import QTcpSocket

from .receive_thread import ReceiveThread
from shared.signals import Signals, SignalTypes
from shared.socket_types import SocketType


class Main_Client(QObject):#сделать сигналы которые будет принимать сервер
    def __init__(self):
        self.host = 'localhost'
        self.port = 5555
        self.socket = QTcpSocket()
        self.socket_type = SocketType.ACCOUNT_INITIAL
        if(not self.socket.connectToHost(self.host, self.port)):
            self.socket = None
        else:
            self.messages = []
            self.signals = Signals()
            self.socket.readyRead.connect(self.SlotReadyRead)
        
    def SlotReadyRead(self):
        inp = QDataStream(self.socket)
        if(inp.status() is not QDataStream.Status.Ok):
            return
        response : str
        signal_type : int
        signal_type = inp.readInt32()
        response = inp.readString()
        match signal_type:
            case SignalTypes.CHECK_ACCOUNT:
                if(response):
                    pass
            case SignalTypes.REG_ACCOUNT:
                pass
            case _:#если дефолт то это чаттинг и надо принять сообщение и написать его в ui
                pass


    def connect(self, host, port):#тупо подключение к серверу
        try:
            self.socket.connectToHost(host,port)
            return True

        except:
            print("Connection error")
            return False
        
    def check_account(self, login:str, password:str):#отправить сигнал серверу чтобы сервер проверил на бд акк с данными логином и паролем
        self.signals.check_account.emit(login, password)
    def reg_account(self, login, password):#отправить сигнал серверу чтобы сервер создал на бд акк с данными логином и паролем
        pass
    def send_to_server(self, message):#отправка сообщения конкретному челику
        outp = QDataStream(self.socket)
        if(outp.status() is not QDataStream.Status.Ok):
            return
        print("sent: " + message)
        try:
            self
        except Exception as e:
            error = "Unable to send message '{}'".format(str(e))
            print("[INFO]", error)
    