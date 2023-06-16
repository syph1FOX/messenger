from typing import Optional
from PySide6.QtCore import QObject
from database.db import *

class ChatManager(QObject):
    chatrooms = {}
    def __init__(self, parent: QObject | None = ...) -> None:
        super().__init__(parent)
    
    def identify_chatroom(self, room, author, message, receiver = None):
        if(room in self.chatrooms):
            self.chatrooms[room].sendMessage(author, message)
        else:
            chatroom = ChatRoom(author, receiver)
            self.chatrooms[room] = chatroom
            chatroom.sendMessage(author, message)

class ChatRoom():
    def __init__(self, db:AccountsDB) -> None:
        self.sockets = []
        self.db = db
    def sendMessage(self, author, message):
        self.db
        