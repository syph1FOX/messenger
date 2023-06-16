from abc import abstractmethod
from PySide6.QtCore import QObject, Signal
from PyQt5 import QtCore
from enum import Enum, auto

class SignalTypes(Enum):
    CHECK_ACCOUNT = auto()
    REG_ACCOUNT = auto()
    DEL_CHAT = auto()
    ADD_CHAT = auto()
    GET_MESSAGES = auto()

class Signals(QObject):
    check_account = Signal(str, str)
    reg_account = Signal(str, str, str, str)
    del_chat = Signal(int)
    add_chat = Signal(int, int)
    get_messages = Signal(int)
