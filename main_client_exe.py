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


class Window(QtWidgets.QMainWindow, mmm.Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)

        self.setWindowTitle('Messenger')
        self.setFixedWidth(800)
        self.setFixedHeight(600)

        # при запуске прилоги откроется страница с логином
        self.stackedWidget.setCurrentWidget(self.logining_p)

        # вызов функции отправки сообщения на кнопку
        self.pushButton_send.clicked.connect(self.send_message)

        # при удачной авторизации открывает страницу с 2 вкладками (списком диалогов и ежедневником)
        self.pushButton_logIn.clicked.connect(self.login)
        self.pushButton_Registrate.clicked.connect(self.registrate)

        self.pushButton_newChat.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.messenging))
        # self.pushButton_newChat.clicked.connect(self.get_messages)

        self.pushButton_reg.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.reg_p))
        self.pushButton_backtolog.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.logining_p))
        self.pushButton_backtomenues.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.menues_p))

        self.pushButton_acc_info.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_about))
        self.pushButton_backtomenues_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.menues_p))
        self.pushButton_exit.clicked.connect(self.logout)

        # self.pushButton_send.clicked.connect(self.send_message)
        self.pushButton_send.setIcon(QIcon("E:\\PycharmProjects\\pythonProject2\\send_icon.png"))
        self.pushButton_send.setIconSize(QSize(36, 36))
        self.listWidget_messages = QtWidgets.QListWidget()

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

    def disconnect_response(self):
        self.label_error.setText("Клиент отключен от сервера")

    def login(self):
        self.init_client()
        if(not self.client.isConnected and not self.client.connect()):
            self.label_error.setText("Ошибка подключения к серверу")
            return
        self.nickname = user_nickname = self.lineEdit_logID.text()
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
        self.nickname = ""
        self.client.disconnect()
        self.listWidget_chats.clear()
        self.stackedWidget.setCurrentWidget(self.logining_p)

    def registrate(self):  # для кнопки Создать аккаунт
        self.nickname = user_login = self.lineEdit_makeID.text()
        user_name = self.lineEdit_makeName.text()
        user_password = self.lineEdit_makePas.text()
        user_mail = self.lineEdit_makeMail.text()
        self.init_client()
        if(not self.client.isConnected and not self.client.connect()):
            self.stackedWidget.setCurrentWidget(self.logining_p)
            self.label_error.setText("Регистрация не удалась")
            return

        if user_login == '' or user_name == '' or user_password == '':
            self.stackedWidget.setCurrentWidget(self.logining_p)
            self.label_error.setText("Введено недостаточно данных")
            return
        
        self.client.reg_account(user_login, user_password, user_name, user_mail)

    def registrate_response(self, response:bool):
        if(response):
            self.open_menues()
        else:
            self.label_error.setText("Регистрация не удалась")

    def open_menues(self):  # для кнопки залогиниться
        self.calendar_db = sqlite3.connect(os.getcwd()+"\\data.db")
        cursor = self.calendar_db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS tasks(username TEXT, task TEXT, date TEXT, completed TEXT)")
        self.calendar_db.commit()
        self.calendarDateChanged()
        self.stackedWidget.setCurrentWidget(self.menues_p)
        self.get_chats()

    # для работы с сообщениями
    def show_messages(self, message1):
        item = QtWidgets.QListWidgetItem()

        if message1['name'] == "USER":
            item.setTextAlignment(Qt.AlignRight)
        item.setText(f"{message1['text']}\n{message1['time']}")
        self.listWidget_messages.addItem(item)


    def get_messages(self, message):
        for i in range(len(message)):
            self.show_messages(message[i])
            # self.after = messages[i]['time']
            self.listWidget_messages.scrollToBottom()
        # pass

    def send_message(self):
        your_message = self.lineEdit_makeMessage.text()
        # self.textBrowser.append('\nYou:\n' + self.lineEdit_makeMessage.text())
        # your_message.setTextAlignment(Qt.AlignRight)
        self.textBrowser.append('\nYou:\n' + your_message)

    #  для работы со списком чатов
    def get_chats(self):
        self.client.get_chats(self.nickname)

    def show_chats(self, chats:list):
        for chat in chats:
            item_chat = QtWidgets.QListWidgetItem()
            item_chat.setText(chat)
            self.listWidget_chats.addItem(item_chat)


    def new_chat(self):
        pass

    def open_dialog(self):  # открытие конкретного чата
        pass

    # для ежедневника
    def calendarDateChanged(self):
        dateSelected = self.calendarWidget.selectedDate().toPython()
        self.updateTaskList(dateSelected)

    def updateTaskList(self, date:date):
        self.tasksListWidget.clear()
        cursor = self.calendar_db.cursor()

        query = "SELECT task, completed FROM tasks WHERE date = ? AND username = ?"
        row = (date.__str__(), self.nickname,)
        results = cursor.execute(query, row).fetchall()
        query = "SELECT * from tasks"
        for result in results:
            item = QListWidgetItem(str(result[0]))
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            if result[1] == "YES":
                item.setCheckState(QtCore.Qt.Checked)
            elif result[1] == "NO":
                item.setCheckState(QtCore.Qt.Unchecked)
            self.tasksListWidget.addItem(item)

    def saveChanges(self):
        cursor = self.calendar_db.cursor()
        date = self.calendarWidget.selectedDate().toPyDate()

        for i in range(self.tasksListWidget.count()):
            item = self.tasksListWidget.item(i)
            task = item.text()
            if item.checkState() == QtCore.Qt.Checked:
                query = "UPDATE tasks SET completed = 'YES' WHERE username = ? AND task = ? AND date = ?"
            else:
                query = "UPDATE tasks SET completed = 'NO' WHERE username = ? AND task = ? AND date = ?"
            row = (self.nickname,task, date,)
            cursor.execute(query, row)
        self.calendar_db.commit()

        messageBox = QMessageBox()
        messageBox.setText("Changes saved.")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()

    def addNewTask(self):
        newTask = str(self.TaskLineEdit.text())
        if(len(newTask) < 1):
            return

        cursor = self.calendar_db.cursor()
        date = self.calendarWidget.selectedDate().toPyDate()
        query = "INSERT INTO tasks VALUES (?,?,?,?)"
        row = (self.nickname, newTask, date, "NO")
        cursor.execute(query, row)
        self.calendar_db.commit()
        self.updateTaskList(date)
        self.TaskLineEdit.clear()


if __name__ == '__main__':
    App = QtWidgets.QApplication([])
    window = Window()
    window.show()
    sys.exit(App.exec())
