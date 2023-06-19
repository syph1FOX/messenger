from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtGui import QIcon
import mmm
from PySide6.QtGui import QIcon
from PySide6.QtCore import *
from PySide6.QtCore import Qt
import sqlite3
from PySide6.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox
import os, datetime, time, sys
from datetime import date
from client.main_client import Main_Client, DB_CheckAccountResponse
from psycopg2 import DATETIME


class Window(QtWidgets.QMainWindow, mmm.Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)

        self.setWindowTitle('Messenger')
        self.setFixedWidth(800)
        self.setFixedHeight(600)

        # при запуске прилоги откроется страница с логином
        self.stackedWidget.setCurrentWidget(self.logining_p)

        # отправка сообщения
        self.pushButton_send.clicked.connect(self.send_message)
        self.lineEdit_makeMessage.returnPressed.connect(self.send_message)

        # авторизация / регистрация
        self.pushButton_logIn.clicked.connect(self.login)
        self.pushButton_Registrate.clicked.connect(self.registrate)
        self.pushButton_reg.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.reg_p))
        self.pushButton_backtolog.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.logining_p))

        # чаты
        self.pushButton_newChat.clicked.connect(self.new_chat)
        self.listWidget_chats.itemClicked.connect(self.open_dialog)

        #возврат в меню
        self.pushButton_backtomenues.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.menues_p))

        #настройка аккаунта
        self.pushButton_acc_info.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_about))
        self.pushButton_acc_info.clicked.connect(self.get_account_info)
        self.pushButton_savechanges.clicked.connect(self.save_account_info)
        self.pushButton_backtomenues_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.menues_p))

        #выход
        self.pushButton_exit.clicked.connect(self.logout)

        #кнопка отправки сообщения
        # self.pushButton_send.clicked.connect(self.send_message)
        self.pushButton_send.setIcon(QIcon("C:\\Users\\Mikhail\\Downloads\\Mess_qstackedw\\messenger\\icon\\icon_send_message.png"))
        self.pushButton_send.setIconSize(QSize(36, 36))

        # для ежедневника
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        self.saveButton.clicked.connect(self.saveChanges)
        self.addButton.clicked.connect(self.addNewTask)
    
        self.client = None

    def init_client(self):
        if(self.client is None):
            self.client = Main_Client()
            self.client.signals.disconnect_from_server.connect(self.disconnect_response)
            self.client.signals.check_account.connect(self.login_response)
            self.client.signals.reg_account.connect(self.registrate_response)
            self.client.signals.get_chats.connect(self.show_chats)
            self.client.signals.get_messages.connect(self.show_messages)
            self.client.signals.change_account_info.connect(self.sace_account_info_response)
            self.client.signals.create_chat.connect(self.create_chat_response)
            self.client.signals.delete_chat.connect(self)

    def save_account_info(self):#для кнопки сохранить в настройках
        print("save_account_info")
        name = self.lineEdit_infoName.text()
        password = self.lineEdit_infoPas.text()
        email = self.lineEdit_infoMail.text()
        self.client.change_info(name, password, email)
        #self.stackedWidget.setCurrentWidget(self.menues_p)

    def sace_account_info_response(self, response:bool):
        if(response):
            print("Данные аккаунта успешно изменены")
            self.client.get_accinfo()
        else:
            print("Не удалось изменить данные аккаунта")

    def get_account_info(self):#для настройки аккаунта
        self.lineEdit_infoName.setText(self.client.account_info['name'])
        if(self.client.account_info['email'] is not None):
            self.lineEdit_infoMail.setText(self.client.account_info['email'])
        self.lineEdit_infoPas.setText(self.client.account_info['password'])
        self.label_infoID.setText(self.client.account_info['login'])

    def disconnect_response(self):
        self.label_error.setText("Клиент отключен от сервера")

    def login(self):
        self.init_client()
        if(not self.client.isConnected and not self.client.connect()):
            self.label_error.setText("Ошибка подключения к серверу")
            return
        self.client.account_nickname = user_nickname = self.lineEdit_logID.text()
        user_password = self.lineEdit_logPas.text()

        if user_nickname == '' or user_password == '':
            self.label_error.setText("Введен некоректный ID или пароль")
            return
        
        self.client.check_account(user_nickname, user_password)
    
    def login_response(self, response:DB_CheckAccountResponse):
        if(response == DB_CheckAccountResponse.OK):
            self.open_menues()
        else:
            self.label_error.setText("Введен некоректный ID или пароль")

    def logout(self):
        self.client.disconnect()
        self.listWidget_chats.clear()
        self.lineEdit_newlogin.clear()
        self.stackedWidget.setCurrentWidget(self.logining_p)

    def registrate(self): 
        self.init_client()
        self.client.account_nickname = user_login = self.lineEdit_makeID.text()
        user_name = self.lineEdit_makeName.text()
        user_password = self.lineEdit_makePas.text()
        user_mail = self.lineEdit_makeMail.text()
        if(not self.client.isConnected and not self.client.connect()):
            self.stackedWidget.setCurrentWidget(self.logining_p)
            self.label_error.setText("Регистрация не удалась")
            return
        if user_login == '' or user_name == '' or user_password == '':
            self.stackedWidget.setCurrentWidget(self.logining_p)
            self.label_error.setText("Введено недостаточно данных")
            return
        if not user_mail.__contains__("@"):
            self.stackedWidget.setCurrentWidget(self.logining_p)
            self.label_error.setText("Введенн некорректный адрес почты")
            return
        
        self.client.reg_account(user_login, user_password, user_name, user_mail)

    def registrate_response(self, response:bool):
        if(response):
            self.open_menues()
        else:
            self.label_error.setText("Регистрация не удалась")
            self.stackedWidget.setCurrentWidget(self.logining_p)

    def open_menues(self):  # для кнопки залогиниться
        self.calendar_db = sqlite3.connect(os.getcwd()+"\\data.db")
        cursor = self.calendar_db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS tasks(username TEXT, task TEXT, date TEXT, completed TEXT)")
        self.calendar_db.commit()
        self.calendarDateChanged()
        self.stackedWidget.setCurrentWidget(self.menues_p)
        self.get_chats()

    # для работы с сообщениями
    def open_dialog(self, item:QListWidgetItem):
        self.another = item.text()
        self.label.setText(self.another)
        self.get_messages(self.another)
        self.stackedWidget.setCurrentWidget(self.messenging)
        self.client.open_chatroom(self.another)

    def close_dialog(self):
        self.listWidget_messages.clear()
        self.client.close_chatroom()
    
    def get_message(self):#если получил сообщение в открытом диалоге
        pass

    def show_messages(self, messages:dict):
        self.listWidget_messages.clear()
        for message in messages:
            item = QtWidgets.QListWidgetItem()
            if(message['author'] == self.client.account_id):
                item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
                item.setText(f"{self.client.account_nickname}:\n{message['body']}\n{message['date']}")
            else:
                item.setTextAlignment(Qt.AlignmentFlag.AlignLeft)
                item.setText(f"{self.another}:\n{message['body']}\n{message['date']}")
            self.listWidget_messages.addItem(item)

    def get_messages(self, another_nickname):#another_nickname - както получать из ui
        self.client.get_messages(another_nickname)

    def send_message(self):
        your_message = self.lineEdit_makeMessage.text()
        if(your_message.__len__ < 1):
            return
        item = QtWidgets.QListWidgetItem()
        item.setText(self.client.account_nickname + "\n" + your_message + "\n")#+время как-то
        item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
        self.listWidget_messages.addItem(item)
        self.lineEdit_makeMessage.setText('')
        self.client

    #  для работы со списком чатов
    def get_chats(self):
        self.client.get_chats()

    def show_chats(self, chats:dict):
        self.listWidget_chats.clear()
        self.client.chat_rooms = chats
        for chat in chats:
            item_chat = QtWidgets.QListWidgetItem()
            item_chat.setText(chats[chat])
            self.listWidget_chats.addItem(item_chat)

    def new_chat(self):
        new_chat = self.lineEdit_newlogin.text()
        print(new_chat)
        self.client.create_chat(new_chat)

    def del_chat_response(self, response:bool):
        if(response):
            print("Чат удален")
        else:
            print("Не удалось удалить чат")

    def create_chat_response(self, response:bool):
        if(response):
            self.get_chats()
            self.lineEdit_newlogin.setText("")
        else:
            print("Не удалось создать чат")

    # для ежедневника
    def calendarDateChanged(self):
        dateSelected = self.calendarWidget.selectedDate().toPython()
        self.updateTaskList(dateSelected)

    def updateTaskList(self, date:date):
        self.tasksListWidget.clear()
        cursor = self.calendar_db.cursor()

        query = "SELECT task, completed FROM tasks WHERE date = ? AND username = ?"
        row = (date.__str__(), self.client.account_nickname)
        results = cursor.execute(query, row).fetchall()
        query = "SELECT * from tasks"
        for result in results:
            item = QListWidgetItem(str(result[0]))
            item.setFlags(item.flags() | QtCore.Qt.ItemFlag.ItemIsUserCheckable)
            if result[1] == "YES":
                item.setCheckState(QtCore.Qt.CheckState.Checked)
            elif result[1] == "NO":
                item.setCheckState(QtCore.Qt.CheckState.Unchecked)
            self.tasksListWidget.addItem(item)

    def saveChanges(self):
        cursor = self.calendar_db.cursor()
        date = self.calendarWidget.selectedDate().toPython()

        for i in range(self.tasksListWidget.count()):
            item = self.tasksListWidget.item(i)
            task = item.text()
            if item.checkState() == QtCore.Qt.CheckState.Checked:
                query = "UPDATE tasks SET completed = 'YES' WHERE username = ? AND task = ? AND date = ?"
            else:
                query = "UPDATE tasks SET completed = 'NO' WHERE username = ? AND task = ? AND date = ?"
            row = (self.client.account_nickname,task, date)
            cursor.execute(query, row)
        self.calendar_db.commit()

        messageBox = QMessageBox()
        messageBox.setText("Changes saved.")
        messageBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        messageBox.exec()

    def addNewTask(self):
        newTask = str(self.TaskLineEdit.text())
        if(len(newTask) < 1):
            return

        cursor = self.calendar_db.cursor()
        date = self.calendarWidget.selectedDate().toPython()

        query = "INSERT INTO tasks VALUES (?,?,?,?)"
        row = (self.client.account_nickname, newTask, date, "NO")
        cursor.execute(query, row)
        self.calendar_db.commit()
        self.updateTaskList(date)
        self.TaskLineEdit.clear()


if __name__ == '__main__':
    App = QtWidgets.QApplication([])
    window = Window()
    window.show()
    sys.exit(App.exec())
