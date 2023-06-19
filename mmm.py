# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mmm.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QFrame, QGraphicsView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStackedWidget, QStatusBar, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: #12181B;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 781, 561))
        self.stackedWidget.setStyleSheet(u"")
        self.logining_p = QWidget()
        self.logining_p.setObjectName(u"logining_p")
        self.lineEdit_logID = QLineEdit(self.logining_p)
        self.lineEdit_logID.setObjectName(u"lineEdit_logID")
        self.lineEdit_logID.setGeometry(QRect(260, 160, 221, 41))
        self.lineEdit_logID.setStyleSheet(u"background-color: #454E56;\n"
"border: 4p\u0445 solid #A9A9A90;\n"
"border-radius: 16;\n"
"padding: 4;\n"
"color: white;")
        self.lineEdit_logID.setMaxLength(8)
        self.label_logPas = QLabel(self.logining_p)
        self.label_logPas.setObjectName(u"label_logPas")
        self.label_logPas.setGeometry(QRect(270, 220, 81, 16))
        font = QFont()
        self.label_logPas.setFont(font)
        self.label_logPas.setStyleSheet(u"color: #BEBFC1;\n"
"font-size: 16px;\n"
"background-color: #2A2E35;")
        self.label_voiti = QLabel(self.logining_p)
        self.label_voiti.setObjectName(u"label_voiti")
        self.label_voiti.setGeometry(QRect(320, 80, 111, 51))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        self.label_voiti.setFont(font1)
        self.label_voiti.setStyleSheet(u"color: white;\n"
"font-family: 'Arial';\n"
"font-size: 40px;\n"
"background-color: #2A2E35;")
        self.label_nonreg = QLabel(self.logining_p)
        self.label_nonreg.setObjectName(u"label_nonreg")
        self.label_nonreg.setGeometry(QRect(270, 398, 81, 16))
        self.label_nonreg.setMouseTracking(False)
        self.label_nonreg.setStyleSheet(u"color: #BEBFC1;\n"
"background-color: #2A2E35;")
        self.label_nonreg.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_logID = QLabel(self.logining_p)
        self.label_logID.setObjectName(u"label_logID")
        self.label_logID.setGeometry(QRect(270, 140, 41, 16))
        self.label_logID.setFont(font1)
        self.label_logID.setStyleSheet(u"QLabel{\n"
"	font-family: 'Arial';\n"
"	color: #BEBFC1;\n"
"	font-size: 16px;\n"
"	background-color: #2A2E35;\n"
"}\n"
"")
        self.lineEdit_logPas = QLineEdit(self.logining_p)
        self.lineEdit_logPas.setObjectName(u"lineEdit_logPas")
        self.lineEdit_logPas.setGeometry(QRect(260, 240, 221, 41))
        self.lineEdit_logPas.setStyleSheet(u"background-color: #454E56;\n"
"border: 4p\u0445 solid #A9A9A9;\n"
"border-radius: 16;\n"
"padding: 4;\n"
"color: white;")
        self.lineEdit_logPas.setMaxLength(16)
        self.lineEdit_logPas.setEchoMode(QLineEdit.Password)
        self.lineEdit_logPas.setDragEnabled(False)
        self.label_error = QLabel(self.logining_p)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setGeometry(QRect(280, 290, 191, 16))
        self.label_error.setStyleSheet(u"color: red;\n"
"background-color: #2A2E35;")
        self.pushButton_reg = QPushButton(self.logining_p)
        self.pushButton_reg.setObjectName(u"pushButton_reg")
        self.pushButton_reg.setGeometry(QRect(350, 390, 121, 31))
        self.pushButton_reg.setFont(font1)
        self.pushButton_reg.setMouseTracking(True)
        self.pushButton_reg.setStyleSheet(u"padding-bottom: 0;\n"
"border: none;\n"
"color: #30466C;\n"
"background-color: #2A2E35;")
        self.pushButton_logIn = QPushButton(self.logining_p)
        self.pushButton_logIn.setObjectName(u"pushButton_logIn")
        self.pushButton_logIn.setGeometry(QRect(300, 320, 151, 41))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        self.pushButton_logIn.setFont(font2)
        self.pushButton_logIn.setStyleSheet(u"\n"
"background-color: #09C372;\n"
"border-radius: 8;\n"
"color: white;")
        self.graphicsView = QGraphicsView(self.logining_p)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(210, 50, 331, 421))
        self.graphicsView.setStyleSheet(u"border-radius: 48px;\n"
"background-color: #2A2E35;\n"
"box-shadow: -16px black; ")
        self.stackedWidget.addWidget(self.logining_p)
        self.graphicsView.raise_()
        self.lineEdit_logID.raise_()
        self.label_logPas.raise_()
        self.label_voiti.raise_()
        self.label_nonreg.raise_()
        self.label_logID.raise_()
        self.lineEdit_logPas.raise_()
        self.label_error.raise_()
        self.pushButton_reg.raise_()
        self.pushButton_logIn.raise_()
        self.reg_p = QWidget()
        self.reg_p.setObjectName(u"reg_p")
        self.label_registration = QLabel(self.reg_p)
        self.label_registration.setObjectName(u"label_registration")
        self.label_registration.setGeometry(QRect(290, 10, 191, 51))
        self.label_registration.setFont(font1)
        self.label_registration.setStyleSheet(u"color: white;\n"
"font-size: 32px;\n"
"font-family: 'Arial';\n"
"background-color: #2A2E35;")
        self.label_regwarn = QLabel(self.reg_p)
        self.label_regwarn.setObjectName(u"label_regwarn")
        self.label_regwarn.setGeometry(QRect(260, 340, 241, 16))
        self.label_regwarn.setFont(font1)
        self.label_regwarn.setStyleSheet(u"background-color: #2A2E35;\n"
"color: red;")
        self.label_regID = QLabel(self.reg_p)
        self.label_regID.setObjectName(u"label_regID")
        self.label_regID.setGeometry(QRect(240, 200, 81, 16))
        self.label_regID.setFont(font1)
        self.label_regID.setStyleSheet(u"padding: 0;\n"
"font-family: 'Arial';\n"
"font-size: 12px;\n"
"color: #AFB1B3;\n"
"background-color: #2A2E35;\n"
"")
        self.label_regName = QLabel(self.reg_p)
        self.label_regName.setObjectName(u"label_regName")
        self.label_regName.setGeometry(QRect(240, 60, 91, 16))
        self.label_regName.setFont(font1)
        self.label_regName.setStyleSheet(u"padding: 0;\n"
"font-family: 'Arial';\n"
"font-size: 12px;\n"
"color: #AFB1B3;\n"
"background-color: #2A2E35;")
        self.label_regMail = QLabel(self.reg_p)
        self.label_regMail.setObjectName(u"label_regMail")
        self.label_regMail.setGeometry(QRect(240, 130, 71, 16))
        self.label_regMail.setFont(font1)
        self.label_regMail.setStyleSheet(u"padding: 0;\n"
"font-family: 'Arial';\n"
"font-size: 12px;\n"
"color: #AFB1B3;\n"
"background-color: #2A2E35;\n"
"")
        self.label_regPass = QLabel(self.reg_p)
        self.label_regPass.setObjectName(u"label_regPass")
        self.label_regPass.setGeometry(QRect(240, 270, 61, 16))
        self.label_regPass.setFont(font1)
        self.label_regPass.setStyleSheet(u"padding: 0;\n"
"font-family: 'Arial';\n"
"font-size: 12px;\n"
"color: #AFB1B3;\n"
"background-color: #2A2E35;")
        self.pushButton_Registrate = QPushButton(self.reg_p)
        self.pushButton_Registrate.setObjectName(u"pushButton_Registrate")
        self.pushButton_Registrate.setGeometry(QRect(310, 370, 151, 41))
        self.pushButton_Registrate.setStyleSheet(u"background-color: #09C372;\n"
"border-radius: 16px;\n"
"color: white;\n"
"font-family: 'Arial';\n"
"font-size: 14px;\n"
"padding: 4px;")
        self.lineEdit_makeName = QLineEdit(self.reg_p)
        self.lineEdit_makeName.setObjectName(u"lineEdit_makeName")
        self.lineEdit_makeName.setGeometry(QRect(230, 80, 301, 41))
        self.lineEdit_makeName.setStyleSheet(u"background-color: #454E56;\n"
"border: 4p\u0445 solid #A9A9A9;\n"
"border-radius: 16;\n"
"padding: 4;\n"
"dont-family: 'Arial';\n"
"font-size: 12px;\n"
"color: white;\n"
"\n"
"")
        self.lineEdit_makeName.setMaxLength(10)
        self.lineEdit_makeID = QLineEdit(self.reg_p)
        self.lineEdit_makeID.setObjectName(u"lineEdit_makeID")
        self.lineEdit_makeID.setGeometry(QRect(230, 220, 301, 41))
        self.lineEdit_makeID.setStyleSheet(u"background-color: #454E56;\n"
"border: 4p\u0445 solid #A9A9A9;\n"
"border-radius: 16;\n"
"padding: 4;\n"
"dont-family: 'Arial';\n"
"font-size: 12px;\n"
"color: white;")
        self.lineEdit_makeID.setMaxLength(8)
        self.lineEdit_makeMail = QLineEdit(self.reg_p)
        self.lineEdit_makeMail.setObjectName(u"lineEdit_makeMail")
        self.lineEdit_makeMail.setGeometry(QRect(230, 150, 301, 41))
        self.lineEdit_makeMail.setStyleSheet(u"background-color: #454E56;\n"
"border: 4p\u0445 solid #A9A9A9;\n"
"border-radius: 16;\n"
"padding: 4;\n"
"dont-family: 'Arial';\n"
"font-size: 12px;\n"
"color: white;")
        self.lineEdit_makeMail.setMaxLength(16)
        self.lineEdit_makePas = QLineEdit(self.reg_p)
        self.lineEdit_makePas.setObjectName(u"lineEdit_makePas")
        self.lineEdit_makePas.setGeometry(QRect(230, 290, 301, 41))
        self.lineEdit_makePas.setStyleSheet(u"background-color: #454E56;\n"
"border: 4p\u0445 solid #A9A9A9;\n"
"border-radius: 16;\n"
"padding: 4;\n"
"dont-family: 'Arial';\n"
"font-size: 12px;\n"
"color: white;")
        self.lineEdit_makePas.setMaxLength(16)
        self.pushButton_backtolog = QPushButton(self.reg_p)
        self.pushButton_backtolog.setObjectName(u"pushButton_backtolog")
        self.pushButton_backtolog.setGeometry(QRect(10, 20, 161, 41))
        self.pushButton_backtolog.setFont(font1)
        self.pushButton_backtolog.setStyleSheet(u"background-color: #5088E9;\n"
"border-radius: 16px;\n"
"color: white;\n"
"font-family: 'Arial';\n"
"font-size: 14px;\n"
"padding: 4px;")
        self.graphicsView_2 = QGraphicsView(self.reg_p)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setGeometry(QRect(210, 10, 341, 441))
        self.graphicsView_2.setStyleSheet(u"border-radius: 32px;\n"
"background-color: #2A2E35;")
        self.stackedWidget.addWidget(self.reg_p)
        self.graphicsView_2.raise_()
        self.label_registration.raise_()
        self.label_regwarn.raise_()
        self.label_regID.raise_()
        self.label_regName.raise_()
        self.label_regMail.raise_()
        self.label_regPass.raise_()
        self.pushButton_Registrate.raise_()
        self.lineEdit_makeName.raise_()
        self.lineEdit_makeID.raise_()
        self.lineEdit_makeMail.raise_()
        self.lineEdit_makePas.raise_()
        self.pushButton_backtolog.raise_()
        self.page_about = QWidget()
        self.page_about.setObjectName(u"page_about")
        self.label_about = QLabel(self.page_about)
        self.label_about.setObjectName(u"label_about")
        self.label_about.setGeometry(QRect(310, 20, 191, 51))
        self.label_about.setFont(font1)
        self.label_about.setStyleSheet(u"color: white;\n"
"font-size: 32px;\n"
"font-family: 'Arial';\n"
"background-color: #2A2E35;")
        self.lineEdit_infoName = QLineEdit(self.page_about)
        self.lineEdit_infoName.setObjectName(u"lineEdit_infoName")
        self.lineEdit_infoName.setGeometry(QRect(250, 90, 301, 41))
        self.lineEdit_infoName.setStyleSheet(u"background-color: #454E56;\n"
"border: 4p\u0445 solid #A9A9A9;\n"
"border-radius: 16;\n"
"padding: 4;\n"
"dont-family: 'Arial';\n"
"font-size: 12px;\n"
"color: white;\n"
"\n"
"")
        self.lineEdit_infoName.setMaxLength(10)
        self.label_infoName = QLabel(self.page_about)
        self.label_infoName.setObjectName(u"label_infoName")
        self.label_infoName.setGeometry(QRect(260, 70, 91, 16))
        self.label_infoName.setFont(font1)
        self.label_infoName.setStyleSheet(u"padding: 0;\n"
"font-family: 'Arial';\n"
"font-size: 12px;\n"
"color: #AFB1B3;\n"
"background-color: #2A2E35;")
        self.label_infoID = QLabel(self.page_about)
        self.label_infoID.setObjectName(u"label_infoID")
        self.label_infoID.setGeometry(QRect(260, 210, 81, 16))
        self.label_infoID.setFont(font1)
        self.label_infoID.setStyleSheet(u"padding: 0;\n"
"font-family: 'Arial';\n"
"font-size: 12px;\n"
"color: #AFB1B3;\n"
"background-color: #2A2E35;\n"
"")
        self.graphicsView_3 = QGraphicsView(self.page_about)
        self.graphicsView_3.setObjectName(u"graphicsView_3")
        self.graphicsView_3.setGeometry(QRect(230, 20, 341, 441))
        self.graphicsView_3.setStyleSheet(u"border-radius: 32px;\n"
"background-color: #2A2E35;\n"
"")
        self.lineEdit_infoMail = QLineEdit(self.page_about)
        self.lineEdit_infoMail.setObjectName(u"lineEdit_infoMail")
        self.lineEdit_infoMail.setGeometry(QRect(250, 160, 301, 41))
        self.lineEdit_infoMail.setStyleSheet(u"background-color: #454E56;\n"
"border: 4p\u0445 solid #A9A9A9;\n"
"border-radius: 16;\n"
"padding: 4;\n"
"dont-family: 'Arial';\n"
"font-size: 12px;\n"
"color: white;")
        self.lineEdit_infoMail.setMaxLength(16)
        self.label_infoPass = QLabel(self.page_about)
        self.label_infoPass.setObjectName(u"label_infoPass")
        self.label_infoPass.setGeometry(QRect(260, 280, 61, 16))
        self.label_infoPass.setFont(font1)
        self.label_infoPass.setStyleSheet(u"padding: 0;\n"
"font-family: 'Arial';\n"
"font-size: 12px;\n"
"color: #AFB1B3;\n"
"background-color: #2A2E35;")
        self.label_infoMail = QLabel(self.page_about)
        self.label_infoMail.setObjectName(u"label_infoMail")
        self.label_infoMail.setGeometry(QRect(260, 140, 71, 16))
        self.label_infoMail.setFont(font1)
        self.label_infoMail.setStyleSheet(u"padding: 0;\n"
"font-family: 'Arial';\n"
"font-size: 12px;\n"
"color: #AFB1B3;\n"
"background-color: #2A2E35;\n"
"")
        self.label_infoWarn = QLabel(self.page_about)
        self.label_infoWarn.setObjectName(u"label_infoWarn")
        self.label_infoWarn.setGeometry(QRect(280, 350, 241, 16))
        self.label_infoWarn.setFont(font1)
        self.label_infoWarn.setStyleSheet(u"background-color: #2A2E35;\n"
"color: red;")
        self.lineEdit_infoPas = QLineEdit(self.page_about)
        self.lineEdit_infoPas.setObjectName(u"lineEdit_infoPas")
        self.lineEdit_infoPas.setGeometry(QRect(250, 300, 301, 41))
        self.lineEdit_infoPas.setStyleSheet(u"background-color: #454E56;\n"
"border: 4p\u0445 solid #A9A9A9;\n"
"border-radius: 16;\n"
"padding: 4;\n"
"dont-family: 'Arial';\n"
"font-size: 12px;\n"
"color: white;")
        self.lineEdit_infoPas.setMaxLength(16)
        self.pushButton_backtomenues_2 = QPushButton(self.page_about)
        self.pushButton_backtomenues_2.setObjectName(u"pushButton_backtomenues_2")
        self.pushButton_backtomenues_2.setGeometry(QRect(30, 20, 181, 41))
        self.pushButton_backtomenues_2.setFont(font1)
        self.pushButton_backtomenues_2.setStyleSheet(u"background-color: #5088E9;\n"
"border-radius: 16px;\n"
"color: white;\n"
"font-family: 'Arial';\n"
"font-size: 14px;\n"
"padding: 4px;")
        self.pushButton_exit = QPushButton(self.page_about)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setGeometry(QRect(250, 400, 111, 41))
        self.pushButton_exit.setStyleSheet(u"background-color: #FF5F5B;\n"
"border-radius: 16px;\n"
"color: white;\n"
"font-family: 'Arial';\n"
"font-size: 14px;\n"
"padding: 4px;")
        self.pushButton_savechanges = QPushButton(self.page_about)
        self.pushButton_savechanges.setObjectName(u"pushButton_savechanges")
        self.pushButton_savechanges.setGeometry(QRect(380, 400, 171, 41))
        self.pushButton_savechanges.setStyleSheet(u"background-color: #09C372;\n"
"border-radius: 16px;\n"
"color: white;\n"
"font-family: 'Arial';\n"
"font-size: 14px;\n"
"padding: 4px;")
        self.label_3 = QLabel(self.page_about)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 230, 301, 41))
        self.label_3.setStyleSheet(u"background-color: #454E56;\n"
"border: 4p\u0445 solid #A9A9A9;\n"
"border-radius: 16;\n"
"padding: 4;\n"
"dont-family: 'Arial';\n"
"font-size: 12px;\n"
"color: white;")
        self.stackedWidget.addWidget(self.page_about)
        self.graphicsView_3.raise_()
        self.lineEdit_infoMail.raise_()
        self.label_infoPass.raise_()
        self.label_infoMail.raise_()
        self.lineEdit_infoPas.raise_()
        self.label_infoID.raise_()
        self.label_infoName.raise_()
        self.lineEdit_infoName.raise_()
        self.label_about.raise_()
        self.label_infoWarn.raise_()
        self.pushButton_backtomenues_2.raise_()
        self.pushButton_exit.raise_()
        self.pushButton_savechanges.raise_()
        self.label_3.raise_()
        self.menues_p = QWidget()
        self.menues_p.setObjectName(u"menues_p")
        self.tabWidget = QTabWidget(self.menues_p)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 20, 781, 551))
        self.tabWidget.setStyleSheet(u"QTabWidget::tab-bar\n"
"{\n"
"    left: 5px;\n"
"    alignment: left;\n"
"    background-color: #3E3E3E;\n"
"}\n"
"QTabBar::bar{\n"
"	background-color: #12181B;\n"
"	font-family: 'Arial';\n"
"}\n"
"")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.pushButton_newChat = QPushButton(self.tab)
        self.pushButton_newChat.setObjectName(u"pushButton_newChat")
        self.pushButton_newChat.setGeometry(QRect(600, 460, 161, 41))
        self.pushButton_newChat.setStyleSheet(u"background-color: #5088E9;\n"
"border-radius: 16px;\n"
"color: white;\n"
"font-size: 16px;")
        self.listWidget_chats = QListWidget(self.tab)
        self.listWidget_chats.setObjectName(u"listWidget_chats")
        self.listWidget_chats.setGeometry(QRect(10, 10, 581, 491))
        self.listWidget_chats.setStyleSheet(u"background-color: #2A2E35;\n"
"color: white;\n"
"font-family: 'Arial';\n"
"font-size: 20px;")
        self.listWidget_chats.setFrameShadow(QFrame.Sunken)
        self.pushButton_acc_info = QPushButton(self.tab)
        self.pushButton_acc_info.setObjectName(u"pushButton_acc_info")
        self.pushButton_acc_info.setGeometry(QRect(600, 10, 161, 41))
        self.pushButton_acc_info.setStyleSheet(u"background-color: #09C372;\n"
"border-radius: 16px;\n"
"color: white;\n"
"font-size: 16px;")
        self.lineEdit_newlogin = QLineEdit(self.tab)
        self.lineEdit_newlogin.setObjectName(u"lineEdit_newlogin")
        self.lineEdit_newlogin.setGeometry(QRect(600, 380, 161, 41))
        self.lineEdit_newlogin.setStyleSheet(u"background-color: #454E56;\n"
"border: none;\n"
"border-radius: 16px;\n"
"color: white;\n"
"font-size: 12px;\n"
"font-family: 'Arial';\n"
"")
        self.label_makenew = QLabel(self.tab)
        self.label_makenew.setObjectName(u"label_makenew")
        self.label_makenew.setGeometry(QRect(610, 340, 151, 31))
        self.label_makenew.setStyleSheet(u"color: white;\n"
"font-size: 12px;\n"
"font-family: 'Arial';")
        self.label_newwarn = QLabel(self.tab)
        self.label_newwarn.setObjectName(u"label_newwarn")
        self.label_newwarn.setGeometry(QRect(610, 430, 131, 21))
        self.label_newwarn.setStyleSheet(u"color: red;\n"
"font-family: 'Arial';")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.calendarWidget = QCalendarWidget(self.tab_2)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(10, 100, 441, 401))
        font3 = QFont()
        font3.setPointSize(10)
        self.calendarWidget.setFont(font3)
        self.calendarWidget.setStyleSheet(u"background-color: fb5b5d;\n"
"border-radius: 8;\n"
"color: #808080;\n"
"")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 751, 71))
        font4 = QFont()
        font4.setPointSize(19)
        self.label_2.setFont(font4)
        self.label_2.setContextMenuPolicy(Qt.NoContextMenu)
        self.label_2.setStyleSheet(u"color : white;\n"
"border-radius: 8px;\n"
"background-color: #22222e;\n"
"border: 1px solid #afafaf;")
        self.label_2.setTextFormat(Qt.PlainText)
        self.TaskLineEdit = QLineEdit(self.tab_2)
        self.TaskLineEdit.setObjectName(u"TaskLineEdit")
        self.TaskLineEdit.setGeometry(QRect(460, 100, 251, 41))
        self.TaskLineEdit.setFont(font1)
        self.TaskLineEdit.setStyleSheet(u"color : white;\n"
"background-color: #454E56;\n"
"border-radius: 8px;\n"
"font-family: 'Arial';")
        self.tasksListWidget = QListWidget(self.tab_2)
        self.tasksListWidget.setObjectName(u"tasksListWidget")
        self.tasksListWidget.setGeometry(QRect(460, 150, 301, 291))
        self.tasksListWidget.setFont(font3)
        self.tasksListWidget.setStyleSheet(u"color : white;\n"
"background-color: #2A2E35;\n"
"border: none;")
        self.saveButton = QPushButton(self.tab_2)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(460, 450, 301, 51))
        font5 = QFont()
        font5.setPointSize(11)
        self.saveButton.setFont(font5)
        self.saveButton.setStyleSheet(u"QPushButton{	\n"
"	background-color: #09C372;\n"
"	border: none;\n"
"	border-radius: 8;\n"
"	color: white;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #606060\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #DCDCDC\n"
"}")
        self.addButton = QPushButton(self.tab_2)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(720, 100, 41, 41))
        self.addButton.setFont(font)
        self.addButton.setStyleSheet(u"QPushButton{	\n"
"	background-color: #09C372;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	color: white;\n"
"	font-size: 16px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #606060\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #DCDCDC\n"
"}")
        self.tabWidget.addTab(self.tab_2, "")
        self.stackedWidget.addWidget(self.menues_p)
        self.messenging = QWidget()
        self.messenging.setObjectName(u"messenging")
        self.label = QLabel(self.messenging)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 20, 181, 21))
        self.label.setStyleSheet(u"color: white;\n"
"font-size: 24px;")
        self.lineEdit_makeMessage = QLineEdit(self.messenging)
        self.lineEdit_makeMessage.setObjectName(u"lineEdit_makeMessage")
        self.lineEdit_makeMessage.setGeometry(QRect(10, 510, 701, 41))
        self.lineEdit_makeMessage.setStyleSheet(u"background-color: #454E56;\n"
"border: none;\n"
"border-radius: 20px;\n"
"padding-left: 8px;\n"
"color: white;\n"
"font-size: 16px;\n"
"font-family: 'Arial';")
        self.pushButton_send = QPushButton(self.messenging)
        self.pushButton_send.setObjectName(u"pushButton_send")
        self.pushButton_send.setGeometry(QRect(720, 510, 41, 41))
        self.pushButton_send.setStyleSheet(u"border: none;")
        self.pushButton_backtomenues = QPushButton(self.messenging)
        self.pushButton_backtomenues.setObjectName(u"pushButton_backtomenues")
        self.pushButton_backtomenues.setGeometry(QRect(10, 10, 41, 41))
        self.pushButton_backtomenues.setFont(font1)
        self.pushButton_backtomenues.setStyleSheet(u"background-color: #5088E9;\n"
"border-radius: 16px;\n"
"color: white;\n"
"font-family: 'Arial';\n"
"font-size: 14px;\n"
"padding: 4px;")
        self.listWidget_messages = QListWidget(self.messenging)
        self.listWidget_messages.setObjectName(u"listWidget_messages")
        self.listWidget_messages.setGeometry(QRect(10, 60, 761, 441))
        self.listWidget_messages.setStyleSheet(u"background-color:#2A2E35;\n"
"border-radius: 16px;\n"
"border: none;\n"
"color: white;\n"
"font-family: 'Arial';\n"
"font-size: 16px;")
        self.stackedWidget.addWidget(self.messenging)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit_logID.setText("")
        self.lineEdit_logID.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 ID", None))
        self.label_logPas.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_voiti.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.label_nonreg.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430?", None))
        self.label_logID.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.lineEdit_logPas.setText("")
        self.lineEdit_logPas.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_error.setText("")
        self.pushButton_reg.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0430\u043a\u043a\u0430\u0443\u043d\u0442", None))
        self.pushButton_logIn.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.label_registration.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.label_regwarn.setText("")
        self.label_regID.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_regName.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u0438 \u0444\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_regMail.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0447\u0442\u0430", None))
        self.label_regPass.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.pushButton_Registrate.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.lineEdit_makeName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u0438 \u0444\u0430\u043c\u0438\u043b\u0438\u044e*", None))
        self.lineEdit_makeID.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0434\u0443\u043c\u0430\u0439\u0442\u0435 \u043b\u043e\u0433\u0438\u043d*", None))
        self.lineEdit_makeMail.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u043e\u0447\u0442\u0443", None))
        self.lineEdit_makePas.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0434\u0443\u043c\u0430\u0439\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c*", None))
        self.pushButton_backtolog.setText(QCoreApplication.translate("MainWindow", u"< \u041d\u0430\u0437\u0430\u0434", None))
        self.label_about.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0435", None))
        self.lineEdit_infoName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u0438 \u0444\u0430\u043c\u0438\u043b\u0438\u044e*", None))
        self.label_infoName.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u0438 \u0444\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_infoID.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.lineEdit_infoMail.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u043e\u0447\u0442\u0443", None))
        self.label_infoPass.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_infoMail.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0447\u0442\u0430", None))
        self.label_infoWarn.setText("")
        self.lineEdit_infoPas.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0434\u0443\u043c\u0430\u0439\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c*", None))
        self.pushButton_backtomenues_2.setText(QCoreApplication.translate("MainWindow", u"< \u041d\u0430\u0437\u0430\u0434", None))
        self.pushButton_exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.pushButton_savechanges.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Login (\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u043d\u0435\u0432\u043e\u0437\u043c\u043e\u0436\u043d\u044b)", None))
        self.pushButton_newChat.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u043a\u043e\u043d\u0442\u0430\u043a\u0442", None))
        self.pushButton_acc_info.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430", None))
        self.lineEdit_newlogin.setPlaceholderText(QCoreApplication.translate("MainWindow", u"*\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d...", None))
        self.label_makenew.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u0434\u0438\u0430\u043b\u043e\u0433", None))
        self.label_newwarn.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0415\u0436\u0435\u0434\u043d\u0435\u0432\u043d\u0438\u043a", None))
        self.TaskLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u0430\u0434\u0430\u0447\u0443...", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c ", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0415\u0436\u0435\u0434\u043d\u0435\u0432\u043d\u0438\u043a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.lineEdit_makeMessage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435...", None))
        self.pushButton_send.setText("")
        self.pushButton_backtomenues.setText(QCoreApplication.translate("MainWindow", u"<", None))
    # retranslateUi

