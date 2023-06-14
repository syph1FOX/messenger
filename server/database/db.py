from enum import Enum, auto
from typing import Self

import psycopg2
from psycopg2 import sql
from psycopg2 import errors
from supabase import create_client, Client

url = "https://hixdiztoqknyqftpheiz.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhpeGRpenRvcWtueXFmdHBoZWl6Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4MDUzOTIzNywiZXhwIjoxOTk2MTE1MjM3fQ.pBqp6opHHbwsouajOn1A0SQDZ9YAVfJ6tsQ37YM4jeQ"


class DB_CheckAccountResponse(Enum):
    OK = auto()
    WRONG_LOGIN = auto()
    WRONG_PASSWORD = auto()


class AccountsDB():
    
    __database = None
    def __init__(self) -> None:
        if self.__database is None:
            self.__database = create_client(url,key)

    @property
    def DB(self) -> Client:
        if self.__database is None:
            raise RuntimeError("database is not initialized")

        return self.__database
    def accounts_collection(self) -> list:
        data , count = self.DB.table('users').select('*').execute()
        return data[1]

    def get_account_info(self, login: str) -> dict | None:
        data, count = self.DB.table('users').select('*').eq('login', login).execute()
        return data

    def delete_chat(self, chat_id) -> bool:
        try:
            data, count = self.DB.table("chats").delete().eq("chat_id", chat_id).execute()
        except:
            print("Что-то пошло не так или чата с таким id не существует")
            return False
        else:
            print("Чат успешно удален")
        return True
        
    def create_chat(self, u_id1:int, u_id2:int) -> bool:
        try:
            data, count = self.DB.table("chats").select("*").eq("user1_id", u_id1).eq("user2_id", u_id2).execute()
            if(data[1]):
                print("Данный чат уже существует")
                return False
            else:
                data, count = self.DB.table("chats").select("*").eq("user1_id", u_id2).eq("user2_id", u_id1).execute()
                if(data[1]):
                    print("Данный чат уже существует")
                    return False
        except: 
            print("Что-то пошло не так")
            return False
        else:
            response = self.DB.table("chats").insert({"user1_id": f"{u_id1}", "user2_id": f"{u_id2}"}).execute()
            print(response)
        return True

    def send_message(self, chat_id, auth_id, message) -> bool:
        try:
            data, count = self.DB.table('chats').select("*").eq("chat_id", chat_id)
            if(data[1]):
                response = self.DB.table('messages').insert({"related chat":f"{chat_id}","body":f"{message}","author":f"{auth_id}"}).execute()
            #галочка под сообщением в ui
        except:
            print("Сообщение не было отправлено")
            return False
            #условно восклицательный знак в ui
        else:
            print("Сообщение успешно отправлено")
            #две галочки под сообщением в ui
        return True

    def check_account(self, entered_password, username) -> DB_CheckAccountResponse:
        try:
            if(username.find("@") == -1):
                data, count = self.DB.table("users").select("*").eq("login", f"{username}").execute()
            else:
                data, count = self.DB.table("users").select("*").eq("email", f"{username}").execute()
        except:
            print("Что-то пошло не так")
            return DB_CheckAccountResponse.WRONG_LOGIN
        else:
            if(data[1]):
                user_password = data[1][0]["password"]
                if(entered_password != user_password):
                    print("Неверный пароль")
                    return DB_CheckAccountResponse.WRONG_PASSWORD
            else:
                print("Пользователя с данным login/email не существует")
                return DB_CheckAccountResponse.WRONG_LOGIN
        return DB_CheckAccountResponse.OK

    #Сделать дефолтный чат(как избранное в вк)

    def register_account(self, login, name, password, email) -> bool: 
        try:
            response = self.DB.table('users').insert({"email":f"{email}","login":f"{login}","name":f"{name}","password":f"{password}"}).execute()
        except:
            print("Пользователь с такими данными уже существует")
            return False
        else:
            print("Пользователь зарегестрирован")
        return True

    def get_messages(self, chat_id:int) -> list:
        try:
            data, count = self.DB.table('messages').select("*").eq('related_chat', chat_id).execute()
            print(data)
        except:
            print("Что-то пошло не так. Сообщения не найдены")
            return None