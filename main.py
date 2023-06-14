from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon
import mmm
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
import sqlite3
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox
from client import Client



class Window(QtWidgets.QMainWindow, mmm.Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)

        self.setWindowTitle('Messenger')
        self.setFixedWidth(800)
        self.setFixedHeight(600)

        #self.client = Client()

        self.calendar_db = sqlite3.connect("C:\\Users\\Mikhail\\Downloads\\Mess_qstackedw\\messenger\\data.db")
        cursor = self.calendar_db.cursor()
        self.nickname = ""
        cursor.execute("CREATE TABLE IF NOT EXISTS tasks(username TEXT, task TEXT, date TEXT, completed TEXT)")
        self.calendar_db.commit()

        # при запуске прилоги откроется страница с логином
        self.stackedWidget.setCurrentWidget(self.logining_p)

        # вызов функции отправки сообщения на кнопку
        self.pushButton_send.clicked.connect(self.send_message)

        # при удачной авторизации открывает страницу с 2 вкладками (списком диалогов и ежедневником)
        self.pushButton_logIn.clicked.connect(self.login)

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
        self.calendarDateChanged()
        self.saveButton.clicked.connect(self.saveChanges)
        self.addButton.clicked.connect(self.addNewTask)

    def login(self):
        self.nickname = user_nickname = self.lineEdit_logID.text()
        user_password = self.lineEdit_logPas.text()

        if user_nickname == '':
            self.label_error.setText("Введен некоректный ID или пароль")
            return

        if user_password == '':
            self.label_error.setText("Введен некоректный ID или пароль")
            return

        # здесь проверка есть ли такой акк в бд и тд и тп
        self.open_menues()
        return
    def logout(self):
        self.nickname = ""
        self.listWidget_chats.clear()
        self.stackedWidget.setCurrentWidget(self.logining_p)

    def registrate(self):  # для кнопки Создать аккаунт
        # user_name = self.textEdit_makeName.text()
        # user_surname = self.textEdit_makeSurname.text()
        # user_mail = self.textEdit_makeMail.text()
        # user_phone = self.textEdit_makePhone.text()
        # user_id = self.textEdit_makeID.text()
        # user_pass = self.textEdit_makePas.text()
        pass
        # self.reg = Registration()
        # self.reg.show()
        # self.hide()

    def open_menues(self):  # для кнопки залогиниться
        self.stackedWidget.setCurrentWidget(self.menues_p)
        self.get_chats()
        # self.menues = MenuesWindow()
        # self.menues.show()
        # self.hide()

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
        for i in range(5):
            self.show_chats()


    def show_chats(self):
        item_chat = QtWidgets.QListWidgetItem()
        item_chat.setText("chat")
        self.listWidget_chats.addItem(item_chat)


    def new_chat(self):
        pass

    def open_dialog(self):  # открытие конкретного чата
        pass

    # для ежедневника
    def calendarDateChanged(self):
        print("The calendar date was changed.")
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        print("Date selected:", dateSelected)
        self.updateTaskList(dateSelected)

    def updateTaskList(self, date):
        self.tasksListWidget.clear()
        cursor = self.calendar_db.cursor()

        query = " SELECT * from tasks"
        results = cursor.execute(query).fetchall()
        print(results)

        query = "SELECT task, completed FROM tasks WHERE date = ? AND username = ?"
        row = (date, self.nickname,)
        results = cursor.execute(query, row).fetchall()
        print(row)
        print(results)
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
        #print("date = " + date.)
        query = "INSERT INTO tasks VALUES (?,?,?,?)"
        row = (self.nickname, newTask, "NO", date,)
        print(row)
        cursor.execute(query, row)
        self.calendar_db.commit()
        self.updateTaskList(date)
        self.TaskLineEdit.clear()


if __name__ == '__main__':
    App = QtWidgets.QApplication([])
    window = Window()
    window.show()
    App.exec_()
