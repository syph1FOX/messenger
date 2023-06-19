from typing import Optional
from PySide6.QtNetwork import QTcpSocket
from PySide6.QtCore import QObject
from database.db import *

class ChatManager(QObject):
    chatrooms = []
    def __init__(self, parent: QObject | None = ...) -> None:
        super().__init__(parent)
    


    #определение комнаты в которую заходит клиент
    def identify_chatroom(self, socket:QTcpSocket, user1_id:int, user2_id:int):
        for user in self.chatrooms:
            users_in_chatroom = 0
            for user_id in user:
                if(user_id == user1_id or user_id == user2_id):
                    users_in_chatroom += 1
                if(users_in_chatroom == 2):
                    pass

        chatroom = ChatRoom(user1_id, user2_id)
        self.chatrooms.append(chatroom)
    
    #алгоритм:
    #пользователь подключается к chatroom при открытии чата и передает туда свой id и id собеседника(ну там кривовато кнч реализовано id собеседника но допустим пока так)
    #для этого вызывается ф-ия identify_chatroom цель которой определить существует ли комната в которой есть оба id
    #если такая комната есть, то user'у(который и отправил запрос на подкление) в данной комнате присваивается сокет
    #иначе создается комната с id user'а, сокетом user'а  и id собеседника
    #затем когда пользователь кинет запрос на отправку сообщения в текущем чате оно сразу запишется в бд
    #если сокет второго пользователя на момент принятия запроса будет подключен к chatroom то ему сервер перекинет сообщение и у него вызовется сигнал типа new_message

#комната-чат
class ChatRoom():
    def __init__(self, user1_id:int, user2_id:int) -> None:
        self.cur_user_count = 0
        self.users = {user1_id:None, user2_id:None}
    def add_user(self, user_id:int, socket:QTcpSocket):
        self.users[user_id] = socket
        self.cur_user_count += 1
    def remove_user(self, user_id:int):
        self.users[user_id] = None
        self.cur_user_count -= 1