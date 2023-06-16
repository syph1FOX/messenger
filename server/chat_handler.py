from typing import Optional
from PySide6.QtCore import Signal, QObject


class ChatHandler(QObject):
    readyRead = Signal()

    def __init__(self, socket, parent: QObject | None = None) -> None:
        super().__init__(parent)
        self.socket = socket
        self.readyRead.connect(self.ReceiveMessage)

    def ReceiveMessage(self):
        pass

    def SendMessage(self):
        self.socket

    
