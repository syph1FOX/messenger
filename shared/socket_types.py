from enum import Enum, auto

class SocketType(Enum):
    ACCOUNT_INITIAL = auto()
    ACCOUNT_INFO = auto()
    CHAT = auto()
    