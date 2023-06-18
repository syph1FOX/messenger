from PySide6.QtCore import QObject, Signal
from enum import Enum, auto

class SignalTypes(Enum):
    CHECK_ACCOUNT = auto()
    REG_ACCOUNT = auto()
    DEL_CHAT = auto()
    ADD_CHAT = auto()
    GET_MESSAGES = auto()
    GET_CHATS = auto()
    SEND_MESSAGE = auto()

class Signals(QObject):
    check_account = Signal(int)
    disconnect_from_server = Signal()
    reg_account = Signal(bool)
    get_chats = Signal(dict)
    get_messages = Signal(dict)
    #del_chat = Signal()
    #add_chat = Signal(str, str)
    #send_message = Signal()
