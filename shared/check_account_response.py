from enum import IntEnum, auto

class DB_CheckAccountResponse(IntEnum):
    OK = auto()
    WRONG_LOGIN = auto()
    WRONG_PASSWORD = auto()