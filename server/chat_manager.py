from typing import Optional
from PySide6.QtCore import QObject
from database.db import *

class ChatManager(QObject):
    chatrooms = {}
    def __init__(self, parent: QObject | None = ...) -> None:
        super().__init__(parent)
    
    #определение комнаты в которую заходит клиент
    def identify_chatroom(self, room, user1, user2):
        if(room in self.chatrooms):
            pass
        else:
            chatroom = ChatRoom(user1, user2)
            self.chatrooms[room] = chatroom

#комната-чат
class ChatRoom():
    def __init__(self, db:AccountsDB) -> None:
        self.sockets = []
        self.db = db
    def sendMessage(self, author, message):
        self.db
        