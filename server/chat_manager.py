from typing import Optional
from PySide6.QtNetwork import QTcpSocket
from PySide6.QtCore import QObject, QDataStream, QByteArray

from shared.request_enum import Request
from .database.db import AccountsDB

class ChatManager(QObject):
    chatrooms: dict[str, 'ChatRoom'] = {}
    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)
    
    def send_message(self, user_author:int, other_user:int, message):
        if (not (chatroom:= self.chatrooms.get(f'{other_user}{user_author}', None)) and
        not (chatroom:= self.chatrooms.get(f'{user_author}{other_user}', None))):
            return
        
        chatroom.send_message(user_author, message)

    #определение комнаты в которую заходит клиент
    def enter_chatroom(self, socket:QTcpSocket, user1_id:int, user2_id:int):
        if(chatroom:= self.chatrooms.get(f'{user2_id}{user1_id}', None)):
            chatroom.add_user(user1_id, socket)
            return

        chatroom = ChatRoom(user1_id, user2_id)
        chatroom.add_user(user1_id, socket)
        self.chatrooms[f'{user1_id}{user2_id}'] = chatroom
    
    def exit_chatroom(self, user1_id:int, user2_id:int):
        if (not (chatroom:= self.chatrooms.get(f'{user1_id}{user2_id}', None)) and
        not (chatroom:= self.chatrooms.get(f'{user2_id}{user1_id}', None))):
            return
        
        chatroom.remove_user(user1_id)
        if(chatroom.cur_user_count == 0):
            self.chatrooms.pop(f'{user1_id}{user2_id}', None)
            self.chatrooms.pop(f'{user2_id}{user1_id}', None)

#комната-чат
class ChatRoom():
    def __init__(self, user1_id:int, user2_id:int) -> None:
        self.cur_user_count = 0
        self.users:dict[int, QTcpSocket | None] = {user1_id:None, user2_id:None}
    def send_message(self, user, message):
        for u_id in self.users:
            if(u_id != user):
                receiver = u_id
                break
        AccountsDB().send_message(user, receiver, message)
        data = [Request.SENDMESSAGE, user, message]
        block = QByteArray()
        outp = QDataStream(block, QDataStream.OpenModeFlag.WriteOnly)
        try:
            outp.writeQVariant(data)
        except:
            print("Error send to client")
        else:
            for socket in self.users.values():
                if(socket is not None):
                    socket.write(block)
                    socket.waitForBytesWritten()
    def add_user(self, user_id:int, socket:QTcpSocket):
        self.users[user_id] = socket
        self.cur_user_count += 1
    def remove_user(self, user_id:int):
        self.users[user_id] = None
        self.cur_user_count -= 1