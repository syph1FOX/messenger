import sys
from PySide6 import QtCore, QtWidgets, QtNetwork
from PySide6.QtNetwork import QTcpSocket, QTcpServer, QHostAddress
from PySide6.QtCore import QByteArray, Signal, QThread, QDataStream


from shared._signals import Signals, SignalTypes
from shared.request_enum import Request
from shared.slot_storage import SlotStorage
from shared.check_account_response import DB_CheckAccountResponse
from .database.db import AccountsDB

class Server(QTcpServer):
    def __init__(self, server_port:int, parent = None):
        super().__init__(parent)
        self.newConnection.connect(self.comingConnection)
        if(self.listen(port=server_port,address=QHostAddress(QHostAddress.SpecialAddress.LocalHost))):
            print(f"Server running on 'localhost':{server_port}")
        else:
            print("Error starting server")
            print(self.errorString())
            sys.exit(1)
        self.db = AccountsDB()
        self.sockets = []
        self.slot_storage = SlotStorage()

    

    #КАК ПРИВЯЗАТЬ КАСТОМНЫЕ СИГНАЛЫ???
    def comingConnection(self) -> None:
        print('new connection')
        client_socket = self.nextPendingConnection() #тут приходит просто QTcpSocket и не видит кастомных сигналов
        slot = self.slot_storage.create_and_store_slot(f"readyRead_{client_socket.socketDescriptor()}", self.SlotReadyRead, client_socket)
        client_socket.readyRead.connect(slot)
        slot = self.slot_storage.create_and_store_slot(f"delete_socket_{client_socket.socketDescriptor()}", self.SlotDisconnected, client_socket)
        client_socket.disconnected.connect(slot)
        self.sockets.append(client_socket)

    def SlotDisconnected(self, client_socket:QTcpSocket):
        print('disconnect')
        client_socket.disconnected.disconnect(self.slot_storage.pop(f"delete_socket_{client_socket.socketDescriptor()}"))
        self.sockets.remove(client_socket)

    def SlotReadyRead(self, socket):
        receive_stream = QDataStream(socket)
        receive_stream.startTransaction()
        data: list = receive_stream.readQVariant() 
        if(not isinstance(data[0], Request)):
            return
        if(not receive_stream.commitTransaction()):
            return
        match(data[0]):
            case Request.AUTHORISATION:
                self.check_account_slot(socket, data[1], data[2])
            case Request.REGISTRATION:
                self.reg_account_slot(socket, data[1], data[2], data[3], data[4])
            case Request.GETCHATS:
                self.get_chats_slot(socket, data[1])
            case Request.CREATECHAT:
                pass
            case Request.DELETECHAT:
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
        block = QByteArray()
        outp = QDataStream(block, QDataStream.OpenModeFlag.WriteOnly)
        try:
            outp.writeQVariant(data)
        except:
            print("Error send to client")
        else:
            socket.write(block)
        

    #КАК ПОЛУЧАТЬ объект отправитель через сигнал??
    def check_account_slot(self, socket:QTcpSocket, login:str, password:str):
        print("check_account_slot")
        try:
            response = self.db.check_account(password, login) 
        except:
            print("Check acc error")
            response = -1
        data = [Request.AUTHORISATION, response]
        self.SendToClient(socket, data)

    def reg_account_slot(self, socket:QTcpSocket, login: str, name: str, password: str, email: str):
        try:
            response = self.db.register_account(login, name, password, email)
        except:
            print("Reg acc error")
            response = False
        data = [Request.REGISTRATION, response]
        self.SendToClient(socket, data)
    def get_chats_slot(self, socket:QTcpSocket, login:str):
        try:
            response = self.db.get_chats(login)
        except:
            print("Get chats error")
            response = []
        data = [Request.GETCHATS, response]
        self.SendToClient(socket, data)
    def add_chat_slot(self, user1_login: str, user2_login: str):
        try:
            user1_id = self.db.get_account_info(user1_login)
            user1_id = user1_id[1]['u_id']
            user2_id = self.db.get_account_info(user2_login)
            user2_id = user2_id[1]['u_id']
            response = self.db.create_chat(user1_id, user2_id)
        except:
            print("Add chat error")
            response = False
        self.SendToClient(response)
    
    def del_chat_slot(self, chat_id: int):
        try:
            response = self.db.delete_chat(chat_id)
            return response
        except:
            print("Del chat error")
            return False
    def get_messages_slot(self, user1_login: str, user2_login: str):
        try:
            user1_id = self.db.get_account_info(user1_login)
            user1_id = user1_id[1]['u_id']
            user2_id = self.db.get_account_info(user2_login)
            user2_id = user2_id[1]['u_id']
            chat_id = self.db.get_chat_id(user1_id, user2_id)
            messages = self.db.get_messages(chat_id)
        except:
            print("Get mes error")
            messages = []