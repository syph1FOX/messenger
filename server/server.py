from PyQt5 import QtCore, QtWidgets, QtNetwork
from PySide6.QtNetwork import QTcpSocket, QTcpServer
from PySide6.QtCore import QByteArray, Signal, QThread, QDataStream

from database.db import *
from shared.signals import Signals, SignalTypes
from shared.socket_types import SocketType
from shared.slot_storage import SlotStorage
from shared.request_enum import Request

    
class Server(QTcpServer):
    def __init__(self, hostname, port):
        # start server
        try:
            if(self.listen(hostname, port)):
                print("[INFO] Server running on {}:{}".format(hostname, port))
        except:
            print("[INFO]Error starting server")
        
        self.newConnection.connect(self.incomingConnection)
        self.db = AccountsDB()
        self.sockets = []
        self.data = QByteArray()
        self.datastream = QDataStream(self.data)
        self.signals = Signals()
        self.slot_storage = SlotStorage()
        self.messages = []
        self.signals.check_account.connect(self.check_account_slot)
        self.signals.add_chat.connect(self.add_chat_slot)
        self.signals.del_chat.connect(self.del_chat_slot)
        self.signals.reg_account.connect(self.reg_account_slot)
        self.signals.get_messages.connect(self.get_messages_slot)
        self.newConnection.connect(self.comingConnection)
    

    def comingConnection(self) -> None:
        client_socket = self.nextPendingConnection()
        slot = self.slot_storage.create_and_store_slot("readyRead", self.SlotReadyRead, client_socket)
        client_socket.readyRead.connect(self.SlotReadyRead)
        slot = self.slot_storage.create_and_store_slot("delete_socket", self.SlotDisconnected, client_socket)
        client_socket.disconnected.connect(slot)
        self.sockets.insert(client_socket)

    def delete_socket(self):
        for socket in self.sockets:
            if(not socket.isValid()):
                self.clients.remove(socket)
                break
    def SlotDisconnected(self, client_socket):
        client_socket.disconnected.disconnect(self.slot_storage.pop("delete_socket"))
        self.sockets.remove(client_socket)
    def SlotReadyRead(self, socket):
        receive_stream = QDataStream(socket)
        while(True):
            receive_stream.startTransaction()
            request = receive_stream.readQVariant()
            if(request is not Request):
                return
            if(not receive_stream.commitTransaction()):
                return
            match(request):
                case Request.AUTHORISATION:
                    pass
                case Request.REGISTRATION:
                    pass
                case Request.SENDMESSAGE:
                    room = receive_stream.readString()
                    if(not isinstance(room, str)):
                        return
                    author = receive_stream.readString()
                    message = receive_stream.readString()
                    if(not receive_stream.commitTransaction()):
                        return



    def SendToClient(self, socket:QTcpSocket, data): #как-то отправлять данные по потоку данных
        outp = QDataStream(socket)
        outp.writeBytes(data)


    def check_account_slot(self, login:str, password:str):#вместо return sendtoclient
        try:
            response = self.db.check_account(password, login) 
            return response
        except:
            print("Check acc error")
            return -1
    def reg_account_slot(self, login: str, name: str, password: str, email: str):
        try:
            response = self.db.register_account(login=login, name=name, password=password, email=email)
            return response
        except:
            print("Reg acc error")
            return False
    def add_chat_slot(self, user1_id: int, user2_id: int):
        try:
            response = self.db.create_chat(user1_id, user2_id)
            return response
        except:
            print("Add chat error")
            return False
    
    def del_chat_slot(self, chat_id: int):
        try:
            response = self.db.delete_chat(chat_id)
            return response
        except:
            print("Del chat error")
            return False
    def get_messages_slot(self, chat_id: int):
        try:
            self.messages = self.db.get_messages(chat_id)
        except:
            print("Get mes error")
            self.messages = []

if __name__ == "__main__":
    port = 5555
    hostname = "localhost"

    server = Server(hostname, port)