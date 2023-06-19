import psycopg2
from psycopg2 import sql
from psycopg2 import errors
from supabase import create_client, Client

from shared.check_account_response import DB_CheckAccountResponse

url = "https://hixdiztoqknyqftpheiz.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhpeGRpenRvcWtueXFmdHBoZWl6Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4MDUzOTIzNywiZXhwIjoxOTk2MTE1MjM3fQ.pBqp6opHHbwsouajOn1A0SQDZ9YAVfJ6tsQ37YM4jeQ"


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
        try:
            data , count = self.DB.table('users').select('*').execute()
            return data[1]
        except:
            print('Проблема с получением данных аккаунтов')
            return []
        
    def get_account_info(self, login: str) -> dict | None:
        try:
            data, count = self.DB.table('users').select('*').eq('login', login).execute()
            return data
        except:
            print(f'Проблемы с нахождением информации по аккаунту {login}')
            return {}

    def change_account_info(self, login:str, name:str, password:str, email:str) -> bool:
        try:
            data = self.get_account_info(login)
            if(not bool(data)):
                return False
            response = self.DB.table('users').update({'name':name, 'password':password, 'email':email}).eq('login', login).execute()
            print(response)
            return True
        except:
            print(f"Не удалось изменить данные аккаунта{login}")
            return False
    def get_chats(self, login:str) -> dict:
        try:
            chats = {}
            data, count = self.DB.table('users').select('u_id').eq('login', login).execute()
            cur_id = data[1][0]['u_id']
            data, count = self.DB.table('users').select('related_chats').eq('login', login).execute()
            chats_id = data[1][0]['related_chats']
            for chat_id in chats_id:
                data, count = self.DB.table('chats').select('user1_id').eq('chat_id', chat_id).execute()
                another_id = data[1][0]['user1_id']
                if(data[1][0]['user1_id'] == cur_id):
                    data, count = self.DB.table('chats').select('user2_id').eq('chat_id', chat_id).execute()
                    another_id = data[1][0]['user2_id']
                data, count = self.DB.table('users').select('name').eq('u_id', another_id).execute()
                chats[another_id] = data[1][0]['name']
            return chats
        except:
            print(f'Проблемы с нахождением чатов связанные с аккаунтом {login}')
            return {}

    def get_chat_id(self, login1, name2) -> int:
        try:
            data, count = self.DB.table('users').select('u_id').eq('login', login1).execute()
            if(data[1] is None):
                return -1
            u_id1 = data[1][0]['u_id']
            data, count = self.DB.table('users').select('u_id').eq('name', name2).execute()
            if(data[1] is None):
                return -1
            u_id2 = data[1][0]['u_id']
            data, count = self.DB.table('chats').select('chat_id').eq('user1_id', u_id1).eq('user2_id', u_id2).execute()
            if(data[1]):
                return data[1][0]['chat_id']
            else:
                data, count = self.DB.table('chats').select('chat_id').eq('user1_id', u_id2).eq('user2_id', u_id1).execute()
                if(data[1]):
                    return data[1][0]['chat_id']
                else:
                    return -1
        except:
            print('Проблемы с нахождением чата')
            return -1
        
    def delete_chat(self, chat_id) -> bool:
        try:
            data, count = self.DB.table("chats").delete().eq("chat_id", chat_id).execute()
            print("Чат успешно удален")
        except:
            print("Что-то пошло не так или чата с таким id не существует")
            return False
        return True
    
    def create_chat(self, u_id1:int, u_id2:int) -> bool:
        try:
            data, count = self.DB.table("chats").select("*").eq("user1_id", u_id1).eq("user2_id", u_id2).execute()
            print(data)
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
            try:
                self.DB.table("chats").insert({"user1_id": u_id1, "user2_id": u_id2}).execute()

                data, count = self.DB.table("chats").select("*").eq("user1_id", u_id1).eq("user2_id", u_id2).execute()
                new_chatid = data[1][0]['chat_id']

                data, count = self.DB.table("users").select("related_chats").eq("u_id", u_id1).execute()
                relchats = data[1][0]['related_chats']
                if(relchats is None):
                    relchats = []
                relchats.append(new_chatid)
                self.DB.table("users").update({'related_chats':relchats}).eq("u_id", u_id1).execute()

                data, count = self.DB.table("users").select("related_chats").eq("u_id", u_id2).execute()
                relchats = data[1][0]['related_chats']
                if(relchats is None):
                    relchats = []
                relchats.append(new_chatid)
                self.DB.table("users").update({'related_chats':relchats}).eq("u_id", u_id2).execute()
            except:
                self.delete_chat(new_chatid)
                return False
        return True

    def send_message(self, chat_id, auth_id, message) -> bool:
        try:
            data, count = self.DB.table('chats').select("*").eq("chat_id", chat_id)
            if(data[1]):
                response = self.DB.table('messages').insert({"related chat":f"{chat_id}","body":f"{message}","author":f"{auth_id}"}).execute()
                print("Сообщение успешно отправлено")
            else:
                print('Чат не найден')
                return False
            #галочка под сообщением в ui
        except:
            print("Сообщение не было отправлено")
            return False
            #условно восклицательный знак в ui
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
            print("Пользователь зарегестрирован")
        except:
            print("Пользователь с такими данными уже существует")
            return False
        return True

    def get_messages(self, chat_id:int) -> dict:
        try:
            data, count = self.DB.table('messages').select("*").eq('related_chat', chat_id).execute()
            return data[1]
        except:
            print("Что-то пошло не так. Сообщения не найдены")
            return {}