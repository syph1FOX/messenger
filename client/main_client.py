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
        self.account_info = {}
        self.account_nickname = ""
        self.account_id = -1
        self.chat_rooms = {}
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
                    self.account_info = response[2][1][0].copy()
                    self.account_id = self.account_info['u_id']
                self.signals.check_account.emit(response[1])

            case Request.REGISTRATION:
                if(response[1]):
                    print("Successful registration")
                    self.account_info = response[2][1][0].copy()
                    self.account_id = self.account_info['u_id']
                self.signals.reg_account.emit(response[1])

            case Request.GETCHATS:
                self.signals.get_chats.emit(response[1])

            case Request.GETMESSAGES:
                self.signals.get_messages.emit(response[1])

            case Request.GETACCINFO:
                self.account_info = response[1].copy()

            case Request.CHANGEINFO:
                self.signals.change_account_info.emit(response[1])

            case Request.CREATECHAT:
                self.signals.create_chat.emit(response[1])

            case Request.DELETECHAT:
                self.signals.delete_chat.emit(response[1])

            case Request.SENDMESSAGE:#по сути получения нового сообщения в ui(неважно пришло оно получателю или отправителю)
                pass
            

    def connect(self):
        self.socket.connectToHost(self.host, self.port)
        self.isConnected = self.socket.waitForConnected()
        self.chat_rooms = {}
        self.chat_rooms = {}
        self.account_info = {}
        self.account_nickname = ""
        return self.isConnected

    def disconnect(self):
        self.isConnected = False
        self.chat_rooms = {}
        self.account_info = {}
        self.account_nickname = ""
        self.account_id = -1
        self.socket.disconnectFromHost()

    def send_message(self, receiver:str, message:str):
        pass

    def open_chatroom(self):
        pass

    def close_chatroom(self):
        pass
        
    def check_account(self, login:str, password:str):
        data = [Request.AUTHORISATION, login, password]
        self.send_to_server(data)

    def reg_account(self, login:str, password:str, name:str, email:str):
        data = [Request.REGISTRATION, login, name, password, email]
        self.send_to_server(data)

    def change_info(self, name:str, password:str, email:str):
        if(self.account_info['name'] == name and self.account_info['password'] == password and self.account_info['email'] == email):
            print("Введены те же данные")
            return
        if(not email.__contains__("@")):
            print("Некорректный почтовый адресс")
            return
        data = [Request.CHANGEINFO, self.account_nickname, name, password, email]
        self.send_to_server(data)

    def get_chats(self):
        data = [Request.GETCHATS, self.account_nickname]
        self.send_to_server(data)

    def create_chat(self, login:str):
        data = [Request.CREATECHAT, self.account_nickname, login]
        self.send_to_server(data)

    def get_accinfo(self):
        data = [Request.GETACCINFO, self.account_nickname]
        self.send_to_server(data)

    def get_messages(self, user:str):
        data = [Request.GETMESSAGES, self.account_nickname, user]
        self.send_to_server(data)

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
    