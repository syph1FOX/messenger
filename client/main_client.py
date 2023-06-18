from typing import Self
from PySide6.QtCore import QObject, QDataStream, QByteArray
from PySide6.QtNetwork import QTcpSocket, QHostAddress

from shared.request_enum import Request
from shared._signals import Signals
from shared.ABC import QSingleton, Singleton
from shared.check_account_response import DB_CheckAccountResponse

# class Main_ClientBase(QObject, metaclass = QSingleton):
#      pass
class Main_Client(QObject):#сделать сигналы которые будет принимать сервер
    _instance = None
    def __new__(cls) -> Self:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.init()
        return cls._instance
    def init(self):
        self.host = QHostAddress(QHostAddress.SpecialAddress.LocalHost)
        self.port = 5555
        self.socket = QTcpSocket()
        self.signals = Signals()
        self.isConnected = False
        self.socket.readyRead.connect(self.SlotReadyRead)
        self.socket.disconnected.connect(self.signals.disconnect_from_server.emit)
        
    def SlotReadyRead(self):
        response = None
        inp = QDataStream(self.socket)
        if(inp.status() is not QDataStream.Status.Ok):
            return
        inp.startTransaction()
        response = inp.readQVariant()
        if(not isinstance(response[0], Request)):
            print("Incorrect data received by client")
            return
        inp.commitTransaction()
        match response[0]:
            case Request.AUTHORISATION:
                if(response[1] == DB_CheckAccountResponse.OK):
                    print("Succesful authorisation")
                self.signals.check_account.emit(response[1])
            case Request.REGISTRATION:
                if(response[1]):
                    print("Successful registration")
                self.signals.reg_account.emit(response[1])
            case Request.GETCHATS:
                self.signals.get_chats.emit(response[1])
            case Request.CREATECHAT:
                pass
            case Request.DELETECHAT:
                pass
            case Request.SENDMESSAGE:
                pass

    def connect(self):
        self.socket.connectToHost(self.host, self.port)
        self.isConnected = self.socket.waitForConnected()
        return self.isConnected

    def disconnect(self):
        self.isConnected = False
        self.socket.disconnectFromHost()
        
    def check_account(self, login:str, password:str):
        data = []
        data.append(Request.AUTHORISATION)
        data.append(login)
        data.append(password)
        self.send_to_server(data)
    def reg_account(self, login:str, password:str, name:str, email:str):
        data = []
        data.append(Request.REGISTRATION)
        data.append(login)
        data.append(name)
        data.append(password)
        data.append(email)
        self.send_to_server(data)
    def get_chats(self, login:str):
        data = []
        data.append(Request.GETCHATS)
        data.append(login)
        self.send_to_server(data)
    def create_chat(self, login1:str, login2:str):
        self.signals.add_chat.emit(login1, login2)
    def get_messages(self, login1:str, login2:str):
        self.signals.get_messages.emit(login1, login2)

    def send_to_server(self, data):
        block = QByteArray()
        outp = QDataStream(block, QDataStream.OpenModeFlag.WriteOnly)
        if(outp.status() is not QDataStream.Status.Ok):
            return
        try:
            outp.writeQVariant(data)
        except:
            print("Error send message to server")
        else:
            self.socket.write(block)
    