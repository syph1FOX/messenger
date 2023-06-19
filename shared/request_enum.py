from enum import Enum, auto

class Request(Enum):
    AUTHORISATION = auto()
    REGISTRATION = auto()
    SENDMESSAGE = auto()
    CREATECHAT = auto()
    DELETECHAT = auto()
    GETCHATS = auto()
    GETMESSAGES = auto()
    GETACCINFO = auto()
    CHANGEINFO = auto()