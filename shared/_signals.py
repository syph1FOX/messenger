from PySide6.QtCore import QObject, Signal
from enum import Enum, auto

class Signals(QObject):
    check_account = Signal(int)
    disconnect_from_server = Signal()
    reg_account = Signal(bool)
    get_chats = Signal(dict)
    get_messages = Signal(dict)
    delete_chat = Signal(bool)
    create_chat = Signal(bool)
    send_message = Signal(str, str)
    change_account_info = Signal(bool)
