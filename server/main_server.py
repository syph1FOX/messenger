import sys
from PySide6 import QtCore, QtWidgets, QtNetwork
from PySide6.QtNetwork import QTcpSocket, QTcpServer, QHostAddress
from PySide6.QtCore import QByteArray, Signal, QThread, QDataStream


from shared.request_enum import Request
from shared.slot_storage import SlotStorage
from shared.check_account_response import DB_CheckAccountResponse
from .database.db import AccountsDB
from .chat_manager import ChatManager

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
        self.chat_manager = ChatManager()
        self.db = AccountsDB()
        self.sockets = []
        self.slot_storage = SlotStorage()

    
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
            case Request.GETMESSAGES:
                self.get_messages_slot(socket, data[1], data[2])
            case Request.GETACCINFO:
                self.get_accinfo_slot(socket, data[1])
            case Request.CHANGEINFO:
                self.change_info_slot(socket, data[1], data[2], data[3], data[4])
            case Request.CREATECHAT:
                self.create_chat_slot(socket, data[1], data[2])
            case Request.DELETECHAT:
                self.del_chat_slot(socket, data[1])
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
        
    def change_info_slot(self, socket, login, name, password, email):
        try:
            response = self.db.change_account_info(login, name, password, email)
        except:
            response = False
        data = [Request.CHANGEINFO, response]
        self.SendToClient(socket, data)

    def get_accinfo_slot(self,socket:QTcpSocket, login):
        try:
            response = self.db.get_account_info(login)
        except:
            print("Get accinfo error")
        data = [Request.GETACCINFO, response[1][0]]
        self.SendToClient(socket, data)

    def check_account_slot(self, socket:QTcpSocket, login:str, password:str):
        try:
            response = self.db.check_account(password, login)
            acc_info = self.db.get_account_info(login) 
        except:
            print("Check acc error")
            response = -1
        data = [Request.AUTHORISATION, response, acc_info]
        self.SendToClient(socket, data)

    def reg_account_slot(self, socket:QTcpSocket, login: str, name: str, password: str, email: str):
        try:
            response = self.db.register_account(login, name, password, email)
            acc_info = self.db.get_account_info(login)
        except:
            print("Reg acc error")
            response = False
        data = [Request.REGISTRATION, response, acc_info]
        self.SendToClient(socket, data)

    def get_chats_slot(self, socket:QTcpSocket, login:str):
        try:
            response = self.db.get_chats(login)
        except:
            print("Get chats error")
            response = []
        data = [Request.GETCHATS, response]
        self.SendToClient(socket, data)

    def create_chat_slot(self, socket:QTcpSocket, user1_login: str, user2_login: str):
        try:
            user1_id = self.db.get_account_info(user1_login)
            user2_id = self.db.get_account_info(user2_login)
            print(user1_id[1][0]['u_id'])
            print(user2_id[1][0]['u_id'])
            response = self.db.create_chat(user1_id[1][0]['u_id'], user2_id[1][0]['u_id'])
        except:
            print("Add chat error")
            response = False
        data = [Request.CREATECHAT, response]
        self.SendToClient(socket, data)
    
    def del_chat_slot(self, socket:QTcpSocket, chat_id: int):
        try:
            response = self.db.delete_chat(chat_id)
        except:
            print("Del chat error")
            response = False
        data = [Request.DELETECHAT, response]
        self.SendToClient(socket, data)

    def get_messages_slot(self, socket:QTcpSocket, user1_login: str, user2_name: str):
        try:
            chat_id = self.db.get_chat_id(user1_login, user2_name)
            messages = self.db.get_messages(chat_id)
        except:
            print("Get mes error")
            messages = {}
        data = [Request.GETMESSAGES, messages]
        self.SendToClient(socket, data)