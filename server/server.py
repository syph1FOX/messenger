from PyQt5 import QtCore, QtWidgets, QtNetwork
from PySide6.QtNetwork import QTcpSocket, QTcpServer
from PySide6.QtCore import QByteArray, Signal, QThread

from database.db import *
from shared.signals import SignalAndSlotsABC

class SignalSlots(SignalAndSlotsABC):
    def __init__(self, db:AccountsDB) -> None:
        super().__init__()
        self.db = db
    def check_account_slot(self, login: str, password: str) -> DB_CheckAccountResponse:
        return self.db.check_account(password, login)
    def reg_account_slot(self, login: str, name: str, password: str, email: str) -> bool:
        return self.db.register_account(login=login, name=name, password=password, email=email)
    def add_chat_slot(self, user1_id: int, user2_id: int) -> bool:
        return self.db.create_chat(user1_id, user2_id)
    def del_chat_slot(self, chat_id: int) -> bool:
        return self.db.delete_chat(chat_id)
    def get_messages_slot(self, chat_id: int) -> list:
        return self.db.get_messages(chat_id)
    
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
        self.clients = {}
        self.data = QByteArray()
        self.signals = SignalSlots(self.db)

    
    def  incomingConnection(self, handle: int) -> None:
        super().incomingConnection(handle)
        client_socket = self.nextPendingConnection()
        client_socket.readyRead.connect(self.receive_message)
        client_socket.disconnected.connect(client_socket.abort)
        client_socket.disconnected.connect(self.delete_socket)
        self.clients[handle] = client_socket

    @QtCore.pyqtSlot(str, str)
    def check_account():
        pass

    def delete_socket():
        pass

    def receive_message(self, connection, nickname):
        pass


    def send_message(self, message, sender):
        if len(self.clients) > 0:
            for nickname in self.clients:
                if nickname != sender:
                    msg = sender + ": " + message.decode()
                    self.clients[nickname].send(msg.encode())


if __name__ == "__main__":
    port = 5555
    hostname = "localhost"

    server = Server(hostname, port)