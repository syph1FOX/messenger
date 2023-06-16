from enum import StrEnum, auto

class Request(StrEnum):
    AUTHORISATION = auto()
    REGISTRATION = auto()
    SENDMESSAGE = auto()
    CREATECHAT = auto()