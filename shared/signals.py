from abc import abstractmethod
from PySide6.QtCore import QObject
from PyQt5 import QtCore

from client.main_client import Client
from server.server import Server


class SignalAndSlotsABC(QObject):
    def __init__(self) -> None:
        self.check_account =  QtCore.pyqtSignal(types=str,name="check_account")
        self.reg_account =  QtCore.pyqtSignal(types=str, name="reg_account")
        self.del_chat =  QtCore.pyqtSignal(types=int, name="del_chat")
        self.add_chat =  QtCore.pyqtSignal(types=int, name="add_chat")
        self.get_messages =  QtCore.pyqtSignal(types=int, name="get_messages")
        self.connect(signal=self.check_account, method=self.check_account_slot, sender=Client, receiver=Server)
        self.connect(signal=self.reg_account, method=self.reg_account_slot, sender=Client, receiver=Server)
        self.connect(signal=self.del_chat, method=self.del_chat_slot, sender=Client, receiver=Server)
        self.connect(signal=self.add_chat, method=self.add_chat_slot, sender=Client, receiver=Server)
        self.connect(signal=self.get_messages, method=self.get_messages_slot, sender=Client, receiver=Server)
        

    @abstractmethod
    def check_account_slot(self, login:str, password:str):
        raise NotImplementedError()
    
    @abstractmethod
    def reg_account_slot(self, login:str, name:str, password:str, email:str):
        raise NotImplementedError()
    
    @abstractmethod
    def del_chat_slot(self, chat_id:int):
        raise NotImplementedError()
    
    @abstractmethod
    def add_chat_slot(self, user1_id:int, user2_id:int):
        raise NotImplementedError()
    
    @abstractmethod
    def get_messages_slot(self, chat_id:int):
        raise NotImplementedError()