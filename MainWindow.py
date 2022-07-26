from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QFileDialog
import sqlite3, cv2, os, shutil, datetime, smtplib
from email import message


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(970, 604)
        MainWindow.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_18 = QtWidgets.QFrame(self.centralwidget)
        self.frame_18.setGeometry(QtCore.QRect(0, 0, 971, 601))
        self.frame_18.setStyleSheet("QFrame{background-color:rgb(190, 0, 0);border:3px solid black}")
        self.frame_18.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_18.setObjectName("frame_18")
        self.frame_17 = QtWidgets.QFrame(self.frame_18)
        self.frame_17.setGeometry(QtCore.QRect(10, 550, 231, 41))
        self.frame_17.setStyleSheet("background-color:rgb(26, 26, 26)")
        self.frame_17.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_17.setObjectName("frame_17")
        self.btnAbout = QtWidgets.QPushButton(self.frame_17)
        self.btnAbout.setGeometry(QtCore.QRect(0, 5, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btnAbout.setFont(font)
        self.btnAbout.setStyleSheet("color:white;border:none\n"
"")
        self.btnAbout.setFlat(True)
        self.btnAbout.setObjectName("btnAbout")
        self.frame_2 = QtWidgets.QFrame(self.frame_18)
        self.frame_2.setGeometry(QtCore.QRect(240, 40, 721, 551))
        self.frame_2.setStyleSheet("background-color:rgb(26, 26, 26);border:none")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_2)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 721, 511))
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget.setStyleSheet("QStackedWidget{background-color:black;border:3px solid black}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.Home = QtWidgets.QWidget()
        self.Home.setObjectName("Home")
        self.label_4 = QtWidgets.QLabel(self.Home)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 721, 511))
        self.label_4.setStyleSheet("")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("images/141434.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.Home)
        self.Register = QtWidgets.QWidget()
        self.Register.setObjectName("Register")
        self.label_5 = QtWidgets.QLabel(self.Register)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 721, 511))
        self.label_5.setStyleSheet("")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("images/abstract.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.frame_5 = QtWidgets.QFrame(self.Register)
        self.frame_5.setGeometry(QtCore.QRect(90, 12, 551, 481))
        self.frame_5.setStyleSheet("background-color:rgb(57, 57, 57);border-radius:13px")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.btnRegisterStudent = QtWidgets.QPushButton(self.frame_5)
        self.btnRegisterStudent.setGeometry(QtCore.QRect(430, 445, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        self.btnRegisterStudent.setFont(font)
        self.btnRegisterStudent.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(255, 214, 8);\n"
"color:black; border-radius:3px\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : black;\n"
"color:rgb(255, 214, 8)\n"
"}")
        self.btnRegisterStudent.setObjectName("btnRegisterStudent")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setGeometry(QtCore.QRect(0, 0, 551, 51))
        self.frame_6.setStyleSheet("background-color:rgb(26, 26, 26);border-radius:10px")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_7.setGeometry(QtCore.QRect(810, 20, 31, 28))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("color:white")
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 551, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(22)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:white\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_11 = QtWidgets.QLabel(self.frame_5)
        self.label_11.setGeometry(QtCore.QRect(160, 80, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:white")
        self.label_11.setObjectName("label_11")
        self.regfname = QtWidgets.QLineEdit(self.frame_5)
        self.regfname.setGeometry(QtCore.QRect(160, 100, 161, 22))
        self.regfname.setStyleSheet("background-color:white;color:black;border:2px solid black")
        self.regfname.setObjectName("regfname")
        self.label_12 = QtWidgets.QLabel(self.frame_5)
        self.label_12.setGeometry(QtCore.QRect(160, 130, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:white")
        self.label_12.setObjectName("label_12")
        self.regmname = QtWidgets.QLineEdit(self.frame_5)
        self.regmname.setGeometry(QtCore.QRect(160, 150, 161, 22))
        self.regmname.setStyleSheet("background-color:white;color:black;border:2px solid black")
        self.regmname.setObjectName("regmname")
        self.label_13 = QtWidgets.QLabel(self.frame_5)
        self.label_13.setGeometry(QtCore.QRect(160, 180, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color:white")
        self.label_13.setObjectName("label_13")
        self.reglname = QtWidgets.QLineEdit(self.frame_5)
        self.reglname.setGeometry(QtCore.QRect(160, 200, 161, 22))
        self.reglname.setStyleSheet("background-color:white;color:black;border:2px solid black")
        self.reglname.setObjectName("reglname")
        self.label_14 = QtWidgets.QLabel(self.frame_5)
        self.label_14.setGeometry(QtCore.QRect(160, 310, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color:white")
        self.label_14.setObjectName("label_14")
        self.regcourse = QtWidgets.QComboBox(self.frame_5)
        self.regcourse.setGeometry(QtCore.QRect(160, 330, 361, 22))
        self.regcourse.setStyleSheet("background-color:white;color:black;border:2px solid black;border-radius:0px")
        self.regcourse.setObjectName("regcourse")
        self.regyear = QtWidgets.QComboBox(self.frame_5)
        self.regyear.setGeometry(QtCore.QRect(360, 200, 161, 22))
        self.regyear.setStyleSheet("background-color:white;color:black;border:2px solid black;border-radius:0px")
        self.regyear.setObjectName("regyear")
        self.label_15 = QtWidgets.QLabel(self.frame_5)
        self.label_15.setGeometry(QtCore.QRect(360, 180, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color:white")
        self.label_15.setObjectName("label_15")
        self.regage = QtWidgets.QLineEdit(self.frame_5)
        self.regage.setGeometry(QtCore.QRect(360, 250, 161, 22))
        self.regage.setStyleSheet("background-color:white;color:black;border:2px solid black")
        self.regage.setObjectName("regage")
        self.label_16 = QtWidgets.QLabel(self.frame_5)
        self.label_16.setGeometry(QtCore.QRect(360, 230, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color:white")
        self.label_16.setObjectName("label_16")
        self.regemail = QtWidgets.QLineEdit(self.frame_5)
        self.regemail.setGeometry(QtCore.QRect(160, 250, 161, 22))
        self.regemail.setStyleSheet("background-color:white;color:black;border:2px solid black")
        self.regemail.setObjectName("regemail")
        self.label_17 = QtWidgets.QLabel(self.frame_5)
        self.label_17.setGeometry(QtCore.QRect(160, 230, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color:white")
        self.label_17.setObjectName("label_17")
        self.regcontact = QtWidgets.QLineEdit(self.frame_5)
        self.regcontact.setGeometry(QtCore.QRect(360, 150, 161, 22))
        self.regcontact.setStyleSheet("background-color:white;color:black;border:2px solid black")
        self.regcontact.setObjectName("regcontact")
        self.label_18 = QtWidgets.QLabel(self.frame_5)
        self.label_18.setGeometry(QtCore.QRect(360, 130, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color:white")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame_5)
        self.label_19.setGeometry(QtCore.QRect(160, 360, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color:white")
        self.label_19.setObjectName("label_19")
        self.regaddress = QtWidgets.QTextEdit(self.frame_5)
        self.regaddress.setGeometry(QtCore.QRect(160, 380, 361, 51))
        self.regaddress.setStyleSheet("background-color:white;color:black;border:2px solid black;border-radius:None")
        self.regaddress.setObjectName("regaddress")
        self.frame_4 = QtWidgets.QFrame(self.frame_5)
        self.frame_4.setGeometry(QtCore.QRect(15, 80, 130, 130))
        self.frame_4.setMinimumSize(QtCore.QSize(130, 130))
        self.frame_4.setMaximumSize(QtCore.QSize(130, 130))
        self.frame_4.setStyleSheet("background-color:white;color:black;border:3px solid black")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.ImageButton = QtWidgets.QPushButton(self.frame_4)
        self.ImageButton.setGeometry(QtCore.QRect(10, 10, 110, 110))
        self.ImageButton.setStyleSheet("border:none;background-color:rgb(190, 190, 190);border-radius:0px")
        self.ImageButton.setText("")
        self.ImageButton.setIconSize(QtCore.QSize(110, 110))
        self.ImageButton.setObjectName("ImageButton")
        self.btnUploadProfile = QtWidgets.QPushButton(self.frame_5)
        self.btnUploadProfile.setGeometry(QtCore.QRect(26, 220, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        self.btnUploadProfile.setFont(font)
        self.btnUploadProfile.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(255, 214, 8);\n"
"color:black; border-radius:3px\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : black;\n"
"color:rgb(255, 214, 8)\n"
"}")
        self.btnUploadProfile.setObjectName("btnUploadProfile")
        self.btnTakePicture = QtWidgets.QPushButton(self.frame_5)
        self.btnTakePicture.setGeometry(QtCore.QRect(26, 250, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        self.btnTakePicture.setFont(font)
        self.btnTakePicture.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(255, 214, 8);\n"
"color:black; border-radius:3px\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : black;\n"
"color:rgb(255, 214, 8)\n"
"}")
        self.btnTakePicture.setObjectName("btnTakePicture")
        self.label_20 = QtWidgets.QLabel(self.frame_5)
        self.label_20.setGeometry(QtCore.QRect(360, 80, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color:white")
        self.label_20.setObjectName("label_20")
        self.regbirthdate = QtWidgets.QDateEdit(self.frame_5)
        self.regbirthdate.setGeometry(QtCore.QRect(360, 100, 161, 22))
        self.regbirthdate.setStyleSheet("background-color:white;color:black;border:2px solid black")
        self.regbirthdate.setCalendarPopup(True)
        self.regbirthdate.setDate(QtCore.QDate(2001, 1, 1))
        self.regbirthdate.setObjectName("regbirthdate")
        self.label_34 = QtWidgets.QLabel(self.frame_5)
        self.label_34.setGeometry(QtCore.QRect(160, 280, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color:white")
        self.label_34.setObjectName("label_34")
        self.regmale = QtWidgets.QRadioButton(self.frame_5)
        self.regmale.setGeometry(QtCore.QRect(220, 283, 50, 16))
        self.regmale.setStyleSheet("color:white;")
        self.regmale.setObjectName("regmale")
        self.regfemale = QtWidgets.QRadioButton(self.frame_5)
        self.regfemale.setGeometry(QtCore.QRect(275, 283, 65, 16))
        self.regfemale.setStyleSheet("color:white;")
        self.regfemale.setObjectName("regfemale")
        self.stackedWidget.addWidget(self.Register)
        self.Update = QtWidgets.QWidget()
        self.Update.setObjectName("Update")
        self.label_7 = QtWidgets.QLabel(self.Update)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 721, 511))
        self.label_7.setStyleSheet("")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("images/abstract.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.frame_7 = QtWidgets.QFrame(self.Update)
        self.frame_7.setGeometry(QtCore.QRect(90, 8, 551, 491))
        self.frame_7.setStyleSheet("background-color:rgb(57, 57, 57);border-radius:13px")
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.btnSaveChanges = QtWidgets.QPushButton(self.frame_7)
        self.btnSaveChanges.setGeometry(QtCore.QRect(430, 460, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        self.btnSaveChanges.setFont(font)
        self.btnSaveChanges.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(255, 214, 8);\n"
"color:black; border-radius:3px\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : black;\n"
"color:rgb(255, 214, 8)\n"
"}")
        self.btnSaveChanges.setObjectName("btnSaveChanges")
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        self.frame_8.setGeometry(QtCore.QRect(0, 0, 551, 51))
        self.frame_8.setStyleSheet("background-color:rgb(26, 26, 26);border-radius:10px")
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_8.setGeometry(QtCore.QRect(810, 20, 31, 28))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("color:white")
        self.pushButton_8.setFlat(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_8 = QtWidgets.QLabel(self.frame_8)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 551, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(22)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:white;")
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_21 = QtWidgets.QLabel(self.frame_7)
        self.label_21.setGeometry(QtCore.QRect(160, 95, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color:white")
        self.label_21.setObjectName("label_21")
        self.updfname = QtWidgets.QLineEdit(self.frame_7)
        self.updfname.setGeometry(QtCore.QRect(160, 115, 161, 22))
        self.updfname.setStyleSheet("background-color:white;color:black;border:2px solid black")
        self.updfname.setObjectName("updfname")
        self.label_22 = QtWidgets.QLabel(self.frame_7)
        self.label_22.setGeometry(QtCore.QRect(160, 145, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color:white")
        self.label_22.setObjectName("label_22")
        self.updmname = QtWidgets.QLineEdit(self.frame_7)
        self.updmname.setGeometry(QtCore.QRect(160, 165, 161, 22))
        self.updmname.setStyleSheet("background-color:white;color:black;border:2px solid black")
        self.updmname.setObjectName("updmname")
        self.label_23 = QtWidgets.QLabel(self.frame_7)
        self.label_23.setGeometry(QtCore.QRect(160, 195, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color:white")
        self.label_23.setObjectName("label_23")
        self.updlname = QtWidgets.QLineEdit(self.frame_7)
        self.updlname.setGeometry(QtCore.QRect(160, 215, 161, 22))
        self.updlname.setStyleSheet("background-color:white;color:black;border:2px solid black")
        self.updlname.setObjectName("updlname")
        self.label_24 = QtWidgets.QLabel(self.frame_7)
        self.label_24.setGeometry(QtCore.QRect(160, 325, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color:white")
        self.label_24.setObjectName("label_24")
        self.updcourse = QtWidgets.QComboBox(self.frame_7)
        self.updcourse.setGeometry(QtCore.QRect(160, 345, 361, 22))
        self.updcourse.setStyleSheet("background-color:white;color:black;border:2px solid black;border-radius:0px")
        self.updcourse.setObjectName("updcourse")
        self.updyear = QtWidgets.QComboBox(self.frame_7)
        self.updyear.setGeometry(QtCore.QRect(360, 215, 161, 22))
        self.updyear.setStyleSheet("background-color:white;color:black;border:2px solid black;border-radius:0px")
        self.updyear.setObjectName("updyear")
        self.label_25 = QtWidgets.QLabel(self.frame_7)
        self.label_25.setGeometry(QtCore.QRect(360, 195, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color:white")
        self.label_25.setObjectName("label_25")
        self.updage = QtWidgets.QLineEdit(self.frame_7)
        self.updage.setGeometry(QtCore.QRect(360, 265, 161, 22))
        self.updage.setStyleSheet("background-color:white;color:black;border:2px solid black")
        self.updage.setObjectName("updage")
        self.label_26 = QtWidgets.QLabel(self.frame_7)
        self.label_26.setGeometry(QtCore.QRect(360, 245, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color:white")
        self.label_26.setObjectName("label_26")
        self.updemail = QtWidgets.QLineEdit(self.frame_7)
        self.updemail.setGeometry(QtCore.QRect(160, 265, 161, 22))
        self.updemail.setStyleSheet("background-color:white;color:black;border:2px solid black")
        self.updemail.setObjectName("updemail")
        self.label_27 = QtWidgets.QLabel(self.frame_7)
        self.label_27.setGeometry(QtCore.QRect(160, 245, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color:white")
        self.label_27.setObjectName("label_27")
        self.updcontact = QtWidgets.QLineEdit(self.frame_7)
        self.updcontact.setGeometry(QtCore.QRect(360, 165, 161, 22))
        self.updcontact.setStyleSheet("background-color:white;color:black;border:2px solid black")
        self.updcontact.setObjectName("updcontact")
        self.label_28 = QtWidgets.QLabel(self.frame_7)
        self.label_28.setGeometry(QtCore.QRect(360, 145, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color:white")
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.frame_7)
        self.label_29.setGeometry(QtCore.QRect(160, 375, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color:white")
        self.label_29.setObjectName("label_29")
        self.updaddress = QtWidgets.QTextEdit(self.frame_7)
        self.updaddress.setGeometry(QtCore.QRect(160, 395, 361, 51))
        self.updaddress.setStyleSheet("background-color:white;color:black;border:2px solid black;border-radius:None")
        self.updaddress.setObjectName("updaddress")
        self.frame_11 = QtWidgets.QFrame(self.frame_7)
        self.frame_11.setGeometry(QtCore.QRect(15, 95, 130, 130))
        self.frame_11.setMinimumSize(QtCore.QSize(130, 130))
        self.frame_11.setMaximumSize(QtCore.QSize(130, 130))
        self.frame_11.setStyleSheet("background-color:white;color:black;border:3px solid black")
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_11.setObjectName("frame_11")
        self.ImageButton_2 = QtWidgets.QPushButton(self.frame_11)
        self.ImageButton_2.setGeometry(QtCore.QRect(10, 10, 110, 110))
        self.ImageButton_2.setStyleSheet("border:none;background-color:rgb(190, 190, 190);border-radius:0px")
        self.ImageButton_2.setText("")
        self.ImageButton_2.setIconSize(QtCore.QSize(110, 110))
        self.ImageButton_2.setObjectName("ImageButton_2")
        self.btnUploadProfile_2 = QtWidgets.QPushButton(self.frame_7)
        self.btnUploadProfile_2.setGeometry(QtCore.QRect(26, 235, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        self.btnUploadProfile_2.setFont(font)
        self.btnUploadProfile_2.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(255, 214, 8);\n"
"color:black; border-radius:3px\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : black;\n"
"color:rgb(255, 214, 8)\n"
"}")
        self.btnUploadProfile_2.setObjectName("btnUploadProfile_2")
        self.btnTakePicture_2 = QtWidgets.QPushButton(self.frame_7)
        self.btnTakePicture_2.setGeometry(QtCore.QRect(26, 265, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        self.btnTakePicture_2.setFont(font)
        self.btnTakePicture_2.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(255, 214, 8);\n"
"color:black; border-radius:3px\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : black;\n"
"color:rgb(255, 214, 8)\n"
"}")
        self.btnTakePicture_2.setObjectName("btnTakePicture_2")
        self.label_30 = QtWidgets.QLabel(self.frame_7)
        self.label_30.setGeometry(QtCore.QRect(360, 95, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color:white")
        self.label_30.setObjectName("label_30")
        self.updbirthdate = QtWidgets.QDateEdit(self.frame_7)
        self.updbirthdate.setGeometry(QtCore.QRect(360, 115, 161, 22))
        self.updbirthdate.setStyleSheet("background-color:white;color:black;border:2px solid black")
        self.updbirthdate.setCalendarPopup(True)
        self.updbirthdate.setDate(QtCore.QDate(2001, 1, 1))
        self.updbirthdate.setObjectName("updbirthdate")
        self.label_40 = QtWidgets.QLabel(self.frame_7)
        self.label_40.setGeometry(QtCore.QRect(160, 295, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("color:white")
        self.label_40.setObjectName("label_40")
        self.updmale = QtWidgets.QRadioButton(self.frame_7)
        self.updmale.setGeometry(QtCore.QRect(220, 298, 50, 16))
        self.updmale.setStyleSheet("color:white;")
        self.updmale.setObjectName("updmale")
        self.updfemale = QtWidgets.QRadioButton(self.frame_7)
        self.updfemale.setGeometry(QtCore.QRect(275, 298, 65, 16))
        self.updfemale.setStyleSheet("color:white;")
        self.updfemale.setObjectName("updfemale")
        self.btndeletestudent = QtWidgets.QPushButton(self.frame_7)
        self.btndeletestudent.setGeometry(QtCore.QRect(340, 460, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        self.btndeletestudent.setFont(font)
        self.btndeletestudent.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(255, 0, 0);\n"
"color:rgb(255, 255, 255); border-radius:3px\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : rgb(255, 255, 255);\n"
"color:rgb(255, 0, 0)\n"
"}\n"
"")
        self.btndeletestudent.setObjectName("btndeletestudent")
        self.btnsearchprofile_2 = QtWidgets.QPushButton(self.frame_7)
        self.btnsearchprofile_2.setGeometry(QtCore.QRect(469, 60, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(8)
        self.btnsearchprofile_2.setFont(font)
        self.btnsearchprofile_2.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(255, 214, 8);\n"
"color:black; border-radius:3px\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : black;\n"
"color:rgb(255, 214, 8)\n"
"}")
        self.btnsearchprofile_2.setObjectName("btnsearchprofile_2")
        self.searchprofile_2 = QtWidgets.QLineEdit(self.frame_7)
        self.searchprofile_2.setGeometry(QtCore.QRect(300, 60, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.searchprofile_2.setFont(font)
        self.searchprofile_2.setStyleSheet("background-color:white;color:black;border:1px solid black")
        self.searchprofile_2.setObjectName("searchprofile_2")
        self.stackedWidget.addWidget(self.Update)
        self.List = QtWidgets.QWidget()
        self.List.setObjectName("List")
        self.label_9 = QtWidgets.QLabel(self.List)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 721, 511))
        self.label_9.setStyleSheet("")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("images/abstract.jpg"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.frame_9 = QtWidgets.QFrame(self.List)
        self.frame_9.setGeometry(QtCore.QRect(30, 37, 661, 431))
        self.frame_9.setStyleSheet("background-color:rgb(57, 57, 57);border-radius:10px")
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setGeometry(QtCore.QRect(0, 0, 661, 51))
        self.frame_10.setStyleSheet("background-color:rgb(26, 26, 26)")
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_9.setGeometry(QtCore.QRect(810, 20, 31, 28))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("color:white")
        self.pushButton_9.setFlat(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_10 = QtWidgets.QLabel(self.frame_10)
        self.label_10.setGeometry(QtCore.QRect(0, 0, 661, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(22)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:white\n"
"")
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.btndeleteallstudents = QtWidgets.QPushButton(self.frame_9)
        self.btndeleteallstudents.setGeometry(QtCore.QRect(10, 400, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        self.btndeleteallstudents.setFont(font)
        self.btndeleteallstudents.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(255, 0, 0);\n"
"color:rgb(255, 255, 255); border-radius:3px\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : rgb(255, 255, 255);\n"
"color:rgb(255, 0, 0)\n"
"}\n"
"")
        self.btndeleteallstudents.setObjectName("btndeleteallstudents")
        self.btnviewall = QtWidgets.QPushButton(self.frame_9)
        self.btnviewall.setGeometry(QtCore.QRect(560, 400, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        self.btnviewall.setFont(font)
        self.btnviewall.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(255, 214, 8);\n"
"color:black; border-radius:3px\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : black;\n"
"color:rgb(255, 214, 8)\n"
"}")
        self.btnviewall.setObjectName("btnviewall")
        self.numberofstudents = QtWidgets.QLabel(self.frame_9)
        self.numberofstudents.setGeometry(QtCore.QRect(10, 65, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Impact")
        self.numberofstudents.setFont(font)
        self.numberofstudents.setStyleSheet("color:white")
        self.numberofstudents.setObjectName("numberofstudents")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_9)
        self.tableWidget.setGeometry(QtCore.QRect(10, 90, 641, 301))
        self.tableWidget.setStyleSheet("QTableWidget{background-color:white;color:black;border:2px solid black;}\n"
"QScrollBar{ background-color: rgb(160, 160, 160) } ")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.viewcoursecbox = QtWidgets.QComboBox(self.frame_9)
        self.viewcoursecbox.setGeometry(QtCore.QRect(280, 60, 370, 22))
        self.viewcoursecbox.setStyleSheet("background-color:white;color:black;border:2px solid black; border-radius:0px")
        self.viewcoursecbox.setObjectName("viewcoursecbox")
        self.viewcoursecbox.addItem("")
        self.stackedWidget.addWidget(self.List)
        self.Profile = QtWidgets.QWidget()
        self.Profile.setObjectName("Profile")
        self.label_31 = QtWidgets.QLabel(self.Profile)
        self.label_31.setGeometry(QtCore.QRect(0, 0, 721, 511))
        self.label_31.setStyleSheet("")
        self.label_31.setText("")
        self.label_31.setPixmap(QtGui.QPixmap("images/abstract.jpg"))
        self.label_31.setScaledContents(True)
        self.label_31.setObjectName("label_31")
        self.frame_12 = QtWidgets.QFrame(self.Profile)
        self.frame_12.setGeometry(QtCore.QRect(15, 50, 681, 411))
        self.frame_12.setStyleSheet("background-color:rgb(57, 57, 57);border-radius:13px")
        self.frame_12.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_12.setObjectName("frame_12")
        self.frame_13 = QtWidgets.QFrame(self.frame_12)
        self.frame_13.setGeometry(QtCore.QRect(0, 0, 681, 51))
        self.frame_13.setStyleSheet("background-color:rgb(26, 26, 26)")
        self.frame_13.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_13.setObjectName("frame_13")
        self.label_32 = QtWidgets.QLabel(self.frame_13)
        self.label_32.setGeometry(QtCore.QRect(0, 0, 681, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(22)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color:white\n"
"")
        self.label_32.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.searchprofile = QtWidgets.QLineEdit(self.frame_12)
        self.searchprofile.setGeometry(QtCore.QRect(440, 60, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.searchprofile.setFont(font)
        self.searchprofile.setStyleSheet("background-color:white;color:black;border:1px solid black")
        self.searchprofile.setObjectName("searchprofile")
        self.btnsearchprofile = QtWidgets.QPushButton(self.frame_12)
        self.btnsearchprofile.setGeometry(QtCore.QRect(610, 60, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(8)
        self.btnsearchprofile.setFont(font)
        self.btnsearchprofile.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(255, 214, 8);\n"
"color:black; border-radius:3px\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : black;\n"
"color:rgb(255, 214, 8)\n"
"}")
        self.btnsearchprofile.setObjectName("btnsearchprofile")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame_12)
        self.tableWidget_2.setGeometry(QtCore.QRect(170, 90, 491, 301))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setStyleSheet("background-color:white;color:black;border:2px solid black;border-radius:0px")
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setRowCount(11)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 0, item)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(5000)
        self.tableWidget_2.horizontalHeader().setHighlightSections(True)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(27)
        self.frame_14 = QtWidgets.QFrame(self.frame_12)
        self.frame_14.setGeometry(QtCore.QRect(20, 90, 140, 140))
        self.frame_14.setMinimumSize(QtCore.QSize(140, 140))
        self.frame_14.setStyleSheet("background-color:white;color:black;border:3px solid black")
        self.frame_14.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_14.setObjectName("frame_14")
        self.ImageButton_3 = QtWidgets.QPushButton(self.frame_14)
        self.ImageButton_3.setGeometry(QtCore.QRect(10, 10, 120, 120))
        self.ImageButton_3.setMinimumSize(QtCore.QSize(120, 120))
        self.ImageButton_3.setStyleSheet("border:none;background-color:rgb(190, 190, 190);border-radius:0px")
        self.ImageButton_3.setText("")
        self.ImageButton_3.setIconSize(QtCore.QSize(110, 110))
        self.ImageButton_3.setObjectName("ImageButton_3")
        self.btnsendemail = QtWidgets.QPushButton(self.frame_12)
        self.btnsendemail.setGeometry(QtCore.QRect(22, 240, 137, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        self.btnsendemail.setFont(font)
        self.btnsendemail.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(255, 214, 8);\n"
"color:black; border-radius:3px\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : black;\n"
"color:rgb(255, 214, 8)\n"
"}")
        self.btnsendemail.setObjectName("btnsendemail")
        self.stackedWidget.addWidget(self.Profile)
        self.Email = QtWidgets.QWidget()
        self.Email.setObjectName("Email")
        self.label_35 = QtWidgets.QLabel(self.Email)
        self.label_35.setGeometry(QtCore.QRect(-5, 0, 731, 511))
        self.label_35.setStyleSheet("")
        self.label_35.setText("")
        self.label_35.setPixmap(QtGui.QPixmap("images/abstract.jpg"))
        self.label_35.setScaledContents(True)
        self.label_35.setObjectName("label_35")
        self.frame_15 = QtWidgets.QFrame(self.Email)
        self.frame_15.setGeometry(QtCore.QRect(140, 35, 471, 441))
        self.frame_15.setStyleSheet("background-color:rgb(57, 57, 57);border-radius:13px")
        self.frame_15.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_15.setObjectName("frame_15")
        self.frame_16 = QtWidgets.QFrame(self.frame_15)
        self.frame_16.setGeometry(QtCore.QRect(0, 0, 471, 51))
        self.frame_16.setStyleSheet("background-color:rgb(26, 26, 26)")
        self.frame_16.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_16.setObjectName("frame_16")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_11.setGeometry(QtCore.QRect(810, 20, 31, 28))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("color:white")
        self.pushButton_11.setFlat(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_36 = QtWidgets.QLabel(self.frame_16)
        self.label_36.setGeometry(QtCore.QRect(0, 0, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(22)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("color:white\n"
";border-radius:10px")
        self.label_36.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.lineeditsubject = QtWidgets.QLineEdit(self.frame_15)
        self.lineeditsubject.setGeometry(QtCore.QRect(30, 130, 411, 22))
        self.lineeditsubject.setStyleSheet("background-color:white;color:black;border:2px solid black")
        self.lineeditsubject.setObjectName("lineeditsubject")
        self.label_37 = QtWidgets.QLabel(self.frame_15)
        self.label_37.setGeometry(QtCore.QRect(30, 110, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("color:white")
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.frame_15)
        self.label_38.setGeometry(QtCore.QRect(30, 160, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("color:white")
        self.label_38.setObjectName("label_38")
        self.messagetextedit = QtWidgets.QTextEdit(self.frame_15)
        self.messagetextedit.setGeometry(QtCore.QRect(30, 180, 411, 211))
        self.messagetextedit.setStyleSheet("background-color:white;color:black;border:2px solid black;border-radius:0px")
        self.messagetextedit.setObjectName("messagetextedit")
        self.sendtocombobox = QtWidgets.QComboBox(self.frame_15)
        self.sendtocombobox.setGeometry(QtCore.QRect(30, 80, 411, 22))
        self.sendtocombobox.setStyleSheet("background-color:white;color:black;border:2px solid black; border-radius:0px")
        self.sendtocombobox.setObjectName("sendtocombobox")
        self.label_39 = QtWidgets.QLabel(self.frame_15)
        self.label_39.setGeometry(QtCore.QRect(30, 60, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("color:white")
        self.label_39.setObjectName("label_39")
        self.btnsendemail_2 = QtWidgets.QPushButton(self.frame_15)
        self.btnsendemail_2.setGeometry(QtCore.QRect(378, 405, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        self.btnsendemail_2.setFont(font)
        self.btnsendemail_2.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(255, 214, 8);\n"
"color:black; border-radius:3px\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : black;\n"
"color:rgb(255, 214, 8)\n"
"}")
        self.btnsendemail_2.setObjectName("btnsendemail_2")
        self.stackedWidget.addWidget(self.Email)
        self.btnRegisterStudentPage = QtWidgets.QPushButton(self.frame_2)
        self.btnRegisterStudentPage.setGeometry(QtCore.QRect(320, 520, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(9)
        self.btnRegisterStudentPage.setFont(font)
        self.btnRegisterStudentPage.setStyleSheet("background-color:rgb(218, 218, 218);color:rgb(0, 0, 0)")
        self.btnRegisterStudentPage.setObjectName("btnRegisterStudentPage")
        self.btnUpdateStudentPage = QtWidgets.QPushButton(self.frame_2)
        self.btnUpdateStudentPage.setGeometry(QtCore.QRect(460, 520, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(9)
        self.btnUpdateStudentPage.setFont(font)
        self.btnUpdateStudentPage.setStyleSheet("background-color:rgb(218, 218, 218);color:rgb(0, 0, 0)")
        self.btnUpdateStudentPage.setObjectName("btnUpdateStudentPage")
        self.btnViewStudentpage = QtWidgets.QPushButton(self.frame_2)
        self.btnViewStudentpage.setGeometry(QtCore.QRect(10, 520, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(9)
        self.btnViewStudentpage.setFont(font)
        self.btnViewStudentpage.setStyleSheet("background-color:rgb(218, 218, 218);color:rgb(0, 0, 0)")
        self.btnViewStudentpage.setObjectName("btnViewStudentpage")
        self.btnEmailStudentPage = QtWidgets.QPushButton(self.frame_2)
        self.btnEmailStudentPage.setGeometry(QtCore.QRect(590, 520, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(9)
        self.btnEmailStudentPage.setFont(font)
        self.btnEmailStudentPage.setStyleSheet("background-color:rgb(218, 218, 218);color:rgb(0, 0, 0)")
        self.btnEmailStudentPage.setObjectName("btnEmailStudentPage")
        self.btnViewStudentsProfilePage = QtWidgets.QPushButton(self.frame_2)
        self.btnViewStudentsProfilePage.setGeometry(QtCore.QRect(140, 520, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(9)
        self.btnViewStudentsProfilePage.setFont(font)
        self.btnViewStudentsProfilePage.setStyleSheet("background-color:rgb(218, 218, 218);color:rgb(0, 0, 0)")
        self.btnViewStudentsProfilePage.setObjectName("btnViewStudentsProfilePage")
        self.frame = QtWidgets.QFrame(self.frame_18)
        self.frame.setGeometry(QtCore.QRect(10, 40, 301, 551))
        self.frame.setStyleSheet("background-color:rgb(57, 57, 57);border:none")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.btnHomePage = QtWidgets.QPushButton(self.frame)
        self.btnHomePage.setGeometry(QtCore.QRect(-90, 0, 331, 141))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(24)
        self.btnHomePage.setFont(font)
        self.btnHomePage.setStyleSheet("color:white;border:none\n"
"")
        self.btnHomePage.setFlat(True)
        self.btnHomePage.setObjectName("btnHomePage")
        self.frame_3 = QtWidgets.QFrame(self.frame_18)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 951, 31))
        self.frame_3.setStyleSheet("background-color:rgb(26, 26, 26);border:none")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.btnExitApp = QtWidgets.QPushButton(self.frame_3)
        self.btnExitApp.setGeometry(QtCore.QRect(920, 0, 31, 28))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnExitApp.setFont(font)
        self.btnExitApp.setStyleSheet("color:white;border:none")
        self.btnExitApp.setFlat(True)
        self.btnExitApp.setObjectName("btnExitApp")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(38, 9, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Impact")
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;border:none\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(10, 8, 21, 16))
        self.label_2.setStyleSheet("border:none")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/students.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_6.setGeometry(QtCore.QRect(810, 20, 31, 28))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("color:white")
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.btnMinimizeApp = QtWidgets.QPushButton(self.frame_3)
        self.btnMinimizeApp.setGeometry(QtCore.QRect(890, 0, 31, 28))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnMinimizeApp.setFont(font)
        self.btnMinimizeApp.setStyleSheet("color:white;border:none")
        self.btnMinimizeApp.setFlat(True)
        self.btnMinimizeApp.setObjectName("btnMinimizeApp")
        self.frame.raise_()
        self.frame_17.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.btnViewStudentpage.clicked.connect(lambda: MainWindow.update())
        self.btnViewStudentsProfilePage.clicked.connect(lambda: MainWindow.update())
        self.btnRegisterStudentPage.clicked.connect(lambda: MainWindow.update())
        self.btnUpdateStudentPage.clicked.connect(lambda: MainWindow.update())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.regfname, self.regmname)
        MainWindow.setTabOrder(self.regmname, self.reglname)
        MainWindow.setTabOrder(self.reglname, self.regemail)
        MainWindow.setTabOrder(self.regemail, self.regcourse)
        MainWindow.setTabOrder(self.regcourse, self.regaddress)
        MainWindow.setTabOrder(self.regaddress, self.regbirthdate)
        MainWindow.setTabOrder(self.regbirthdate, self.regcontact)
        MainWindow.setTabOrder(self.regcontact, self.regyear)
        MainWindow.setTabOrder(self.regyear, self.regage)
        MainWindow.setTabOrder(self.regage, self.regmale)
        MainWindow.setTabOrder(self.regmale, self.regfemale)
        MainWindow.setTabOrder(self.regfemale, self.sendtocombobox)
        MainWindow.setTabOrder(self.sendtocombobox, self.lineeditsubject)
        MainWindow.setTabOrder(self.lineeditsubject, self.messagetextedit)
        MainWindow.setTabOrder(self.messagetextedit, self.btnsendemail_2)
        MainWindow.setTabOrder(self.btnsendemail_2, self.btnRegisterStudent)
        MainWindow.setTabOrder(self.btnRegisterStudent, self.pushButton_9)
        MainWindow.setTabOrder(self.pushButton_9, self.btndeleteallstudents)
        MainWindow.setTabOrder(self.btndeleteallstudents, self.tableWidget)
        MainWindow.setTabOrder(self.tableWidget, self.btnExitApp)
        MainWindow.setTabOrder(self.btnExitApp, self.pushButton_6)
        MainWindow.setTabOrder(self.pushButton_6, self.btnviewall)
        MainWindow.setTabOrder(self.btnviewall, self.btnViewStudentpage)
        MainWindow.setTabOrder(self.btnViewStudentpage, self.btnRegisterStudentPage)
        MainWindow.setTabOrder(self.btnRegisterStudentPage, self.btnUpdateStudentPage)
        MainWindow.setTabOrder(self.btnUpdateStudentPage, self.btnMinimizeApp)
        MainWindow.setTabOrder(self.btnMinimizeApp, self.btnEmailStudentPage)
        MainWindow.setTabOrder(self.btnEmailStudentPage, self.btnViewStudentsProfilePage)
        MainWindow.setTabOrder(self.btnViewStudentsProfilePage, self.btnAbout)
        MainWindow.setTabOrder(self.btnAbout, self.searchprofile)
        MainWindow.setTabOrder(self.searchprofile, self.btnsearchprofile)
        MainWindow.setTabOrder(self.btnsearchprofile, self.tableWidget_2)
        MainWindow.setTabOrder(self.tableWidget_2, self.ImageButton_3)
        MainWindow.setTabOrder(self.ImageButton_3, self.pushButton_11)
        MainWindow.setTabOrder(self.pushButton_11, self.ImageButton)
        MainWindow.setTabOrder(self.ImageButton, self.btnUploadProfile)
        MainWindow.setTabOrder(self.btnUploadProfile, self.pushButton_7)
        MainWindow.setTabOrder(self.pushButton_7, self.btnsendemail)
        MainWindow.setTabOrder(self.btnsendemail, self.btnTakePicture)
        MainWindow.setTabOrder(self.btnTakePicture, self.viewcoursecbox)


        self.Commit()

        
    def Commit(self):
        self.btnViewStudentpage.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.btnViewStudentpage.clicked.connect(lambda: self.viewcoursecbox.setCurrentText(' Select course to view'))


        self.btnViewStudentsProfilePage.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))

        self.btnRegisterStudentPage.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

        self.btnUpdateStudentPage.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))

        self.btnEmailStudentPage.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))


        self.btnUploadProfile.clicked.connect(self.UploadImageRegister)
        self.btnUploadProfile_2.clicked.connect(self.UploadImageUpdate)     
        self.btnTakePicture.clicked.connect(self.TakePictureRegister)
        self.btnTakePicture_2.clicked.connect(self.TakePictureUpdate)
        self.ImageButton.clicked.connect(self.ViewProfilePicture)
        self.ImageButton_2.clicked.connect(self.ViewProfilePicture)
        self.ImageButton_3.clicked.connect(self.ViewProfilePicture)
        self.btnAbout.clicked.connect(self.AboutTheApp)
        self.btnHomePage.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        
        self.viewcoursecbox.currentTextChanged.connect(self.ViewListCourse)
        self.btnviewall.clicked.connect(self.ViewList)

        self.regyear.addItem(' Select year level')
        self.updyear.addItem(' Select year level')

        self.regcourse.addItem(' Select course')
        self.updcourse.addItem(' Select course')

        self.yearlvl = ['1','2','3','4','5']
        for year in self.yearlvl:
                self.regyear.addItem(year)
                self.updyear.addItem(year)

        self.courses = [
'Bachelor of Science in Entertainment and Multimedia Computing',        
'Bachelor of Science in Information Technology',
'Bachelor of Science in Computer Science',
'Bachelor of Science in Information Systems',
'Bachelor of Science in Architecture',
'Bachelor of Science in Civil Engineering',
'Bachelor of Science in Industrial Engineering',
'Bachelor of Science in Geodetic Engineering',
'Bachelor of Science in Mechanical Engineering',
'Bachelor of Library and Information Science',
'Bachelor of Science in Entrepreneurship',
'Bachelor of Science in Management',
'Bachelor of Science in Accountancy',
'Bachelor of Science in Business Administration',
'Bachelor of Science in Elementary Education',
'Bachelor of Science in Office Administration',
'Bachelor of Laws',
'Bachelor of Science in Secondary Education',
'Bachelor of Science in Electrical Engineering',
'Bachelor of Science in Computer Engineering',
'Bachelor of Science in Electronics Engineering',
'Bachelor of Science in Liberal Arts-Commerce',
'Bachelor of Science in Marine Transportation',
'Bachelor of Science in Marine Engineering',
'Bachelor of Science in Criminology',
'Bachelor of Science in Hotel and Restaurant Management',
'Bachelor of Science in Tourism',
'Bachelor of Science in Biology',
'Bachelor of Science in Environmental Science',
'Bachelor of Arts',
'Bachelor of Arts in Broadcasting',
'Bachelor of Arts in Communication',
'Bachelor of Arts in Comparative Literature',
'Bachelor of Arts in Economics',
'Bachelor of Arts in English Language',
'Bachelor of Science in Psychology',
'Bachelor of Science in Mass Communication',
'Bachelor of Science in Public Administration',
'Bachelor of Arts in General Science',
'Bachelor of Arts in History',
'Bachelor of Arts in Journalism',
'Bachelor of Arts in Literature',
'Bachelor of Arts in Mathematics',
'Bachelor of Arts in Philosophy',
'Bachelor of Arts in Philippine Literature',
'Bachelor of Arts in Political Science',
'Bachelor of Arts in Sociology',
'Bachelor of Science in Fine Arts'
]
        for course in self.courses:
                self.regcourse.addItem(course)
                self.updcourse.addItem(course)
                self.viewcoursecbox.addItem(course)
        
        self.btnsearchprofile.clicked.connect(self.ViewProfile)
        self.searchprofile.returnPressed.connect(self.ViewProfile)

        self.searchprofile_2.returnPressed.connect(self.SearchUpdate)
        self.btnsearchprofile_2.clicked.connect(self.SearchUpdate)
        self.btnSaveChanges.clicked.connect(self.UpdateValidation)
        self.btndeleteallstudents.clicked.connect(self.DeleteAllValidation)
        self.btndeletestudent.clicked.connect(self.DeleteValidation)
        self.btnsendemail_2.clicked.connect(self.SendEmail)
        self.btnEmailStudentPage.clicked.connect(self.ShowEmails)
        self.btnRegisterStudent.clicked.connect(self.AutomaticNotification)
        self.btnRegisterStudent.clicked.connect(self.Register_)
        self.btnsendemail.clicked.connect(self.SendEmailFromProfile)
        self.ShowEmails()
        self.tableWidget.setEnabled(False)
        self.tableWidget_2.setEnabled(False)

    def SendEmailFromProfile(self):
        if len(self.searchprofile.text()) != 0:
                db = sqlite3.connect('SIS.db')
                cur = db.cursor()
                cur.execute(f'SELECT * FROM students_information WHERE FullName = "{self.searchprofile.text()}"')
                GetInfo = cur.fetchall()
                for info in GetInfo:
                        self.sendtocombobox.setCurrentText(str(info[6]))
                self.stackedWidget.setCurrentIndex((5))

    def AutomaticNotification(self):
        email = "studentinformationsystem101@gmail.com"
        password = "endgcwgcnmbymkbe"

        from_ = 'Student Information System'
        send_to = self.regemail.text()
        subject_ = '[University Name] Admissions'
        student_name = f'{self.regfname.text()} {self.reglname.text()}'
        message_ = f'Dear {student_name},\n\n\
We glad to inform you that you have been successfully admitted to [University Name].\nAs a student of [University Name], you will be joining a community of very talented students and exceptional scholars. This will certainly be a rewarding experience that will have a major impact on your future career and peruse of excellence.\n\n- Automatic notification via Students Information System -'

        msg = message.Message()
        msg.add_header('from',from_)
        msg.add_header('to',self.sendtocombobox.currentText())
        msg.add_header('subject',subject_)
        msg.set_payload(message_)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        server.login(email,password)
        server.send_message(msg,from_addr=email,to_addrs=send_to)

    def ShowEmails(self):
        self.sendtocombobox.clear()
        self.sendtocombobox.addItem("Select email")
        self.sendtocombobox.addItem("Send to all students")
        db = sqlite3.connect('SIS.db')
        cur = db.cursor()
        cur.execute('SELECT * FROM students_information')
        GetInfo = cur.fetchall()
        self.EmailList = []
        self.EmailList.clear()
        for info in GetInfo:
                self.sendtocombobox.addItem(str(info[6]))
                self.EmailList.append(str(info[6]))

    def SendEmail(self):
        if len(self.lineeditsubject.text()) != 0 and len(self.messagetextedit.toPlainText()) != 0:
                try:
                        if self.sendtocombobox.currentText() != "Select email" and self.sendtocombobox.currentText() != "Send to all students":
                                email = "studentinformationsystem101@gmail.com"
                                password = "endgcwgcnmbymkbe"

                                from_ = 'Student Information System'
                                send_to = self.sendtocombobox.currentText()
                                subject_ = self.lineeditsubject.text()
                                message_ = self.messagetextedit.toPlainText()

                                msg = message.Message()
                                msg.add_header('from',from_)
                                msg.add_header('to',self.sendtocombobox.currentText())
                                msg.add_header('subject',subject_)
                                msg.set_payload(message_)

                                server = smtplib.SMTP('smtp.gmail.com', 587)
                                server.starttls()

                                server.login(email,password)
                                server.send_message(msg,from_addr=email,to_addrs=send_to)

                        if self.sendtocombobox.currentText() == "Send to all students":
                                email = "studentinformationsystem101@gmail.com"
                                password = "endgcwgcnmbymkbe"

                                from_ = 'Student Information System'
                                send_to = self.EmailList
                                subject_ = self.lineeditsubject.text()
                                message_ = self.messagetextedit.toPlainText()

                                msg = message.Message()
                                msg.add_header('from',from_)
                                msg.add_header('to',self.sendtocombobox.currentText())
                                msg.add_header('subject',subject_)
                                msg.set_payload(message_)

                                server = smtplib.SMTP('smtp.gmail.com', 587)
                                server.starttls()

                                server.login(email,password)
                                server.send_message(msg,from_addr=email,to_addrs=send_to)

                        self.msg = QMessageBox()
                        self.msg.setWindowTitle(' ')
                        self.msg.setWindowIcon(QtGui.QIcon('images/students.png'))
                        self.msg.setIcon(QMessageBox.Icon.Information)
                        self.msg.setText('Email send successfully.')
                        self.msg.exec()

                except:
                        self.msg = QMessageBox()
                        self.msg.setWindowTitle(' ')
                        self.msg.setWindowIcon(QtGui.QIcon('images/students.png'))
                        self.msg.setIcon(QMessageBox.Icon.Critical)
                        self.msg.setText('Unknow error occured.')
                        self.msg.setInformativeText('Please try again later.')
                        self.msg.exec()

                        

    def DeleteAllValidation(self):
        db = sqlite3.connect('SIS.db')
        cur = db.cursor()
        cur.execute('SELECT * FROM students_information')
        GetInfo = cur.fetchall()
        validation = 0
        for info in GetInfo:
                validation += 1
        if validation != 0:
                self.msg = QMessageBox()
                self.msg.setWindowIcon(QtGui.QIcon('images/students.png'))
                self.msg.setWindowTitle(' ')
                self.msg.setIcon(QMessageBox.Icon.Warning)
                self.msg.setText('Are you sure you want to delete all the records?')
                self.msg.setInformativeText('This action cannot be undone.')
                self.msg.setStandardButtons(QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.Cancel) 
                self.msg.buttonClicked.connect(self.DeleteAll_)    
                self.msg.exec() 

    def DeleteAll_(self,key):
        if key.text() == '&Yes':
                db = sqlite3.connect('SIS.db')
                cur = db.cursor()
                cur.execute('DELETE FROM students_information')
                db.commit()
                cur.execute('UPDATE sqlite_sequence SET seq = 1000')
                db.commit()
                self.ViewList()

    def DeleteValidation(self):
        db = sqlite3.connect('SIS.db')
        cur = db.cursor()
        cur.execute(f'SELECT * FROM students_information WHERE FullName = "{self.searchprofile_2.text()}"')
        GetInfo = cur.fetchall()
        validation = 0
        for info in GetInfo:
                validation += 1
        if validation != 0:
                self.msg = QMessageBox()
                self.msg.setWindowIcon(QtGui.QIcon('images/students.png'))
                self.msg.setWindowTitle(' ')
                self.msg.setIcon(QMessageBox.Icon.Warning)
                self.msg.setText('Are you sure you want to delete this record?')
                self.msg.setInformativeText('This action cannot be undone.')
                self.msg.setStandardButtons(QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.Cancel) 
                self.msg.buttonClicked.connect(self.Delete_)    
                self.msg.exec() 

    def Delete_(self,key):
        if key.text() == '&Yes':
                if os.path.exists('SIS.db'):
                        os.remove('SIS.db')
                        db = sqlite3.connect('SIS.db')
                        cur = db.cursor()
                        cur.execute(f'DELETE FROM students_information WHERE FullName = "{self.searchprofile_2.text()}"')

    def ViewProfile(self):
        if len(self.searchprofile.text()) != 0:
                if os.path.isdir('imageHolder'):
                        shutil.rmtree('imageHolder')
                os.makedirs('imageHolder')
                db = sqlite3.connect('SIS.db')
                cur = db.cursor()
                cur.execute(f'SELECT * FROM students_information WHERE FullName = "{self.searchprofile.text()}"')
                GetInfo = cur.fetchall()   
                validation = 0  
                for info in GetInfo:
                        validation += 1
                        with open('imageHolder/img.png', 'wb') as file:
                                file.write(info[0])
                        self.ImageButton_3.setIcon(QtGui.QIcon('imageHolder/img.png'))
                        self.tableWidget_2.setItem(0,0,QtWidgets.QTableWidgetItem(str(info[1])))
                        self.tableWidget_2.setItem(1,0,QtWidgets.QTableWidgetItem(str(info[2])))
                        self.tableWidget_2.setItem(2,0,QtWidgets.QTableWidgetItem(str(info[3])))
                        self.tableWidget_2.setItem(3,0,QtWidgets.QTableWidgetItem(str(info[4])))
                        self.tableWidget_2.setItem(4,0,QtWidgets.QTableWidgetItem(str(info[13])))
                        self.tableWidget_2.setItem(5,0,QtWidgets.QTableWidgetItem(str(info[9])))
                        self.tableWidget_2.setItem(6,0,QtWidgets.QTableWidgetItem(str(info[6])))
                        self.tableWidget_2.setItem(7,0,QtWidgets.QTableWidgetItem(str(info[10])))
                        self.tableWidget_2.setItem(8,0,QtWidgets.QTableWidgetItem(str(info[7])))
                        self.tableWidget_2.setItem(9,0,QtWidgets.QTableWidgetItem(str(info[11])))
                        self.tableWidget_2.setItem(10,0,QtWidgets.QTableWidgetItem(str(info[8])))

                if validation == 0:
                        self.msg = QMessageBox()
                        self.msg.setWindowIcon(QtGui.QIcon('images/students.png'))
                        self.msg.setWindowTitle(' ')
                        self.msg.setText('No record found.')
                        self.msg.setIcon(QMessageBox.Icon.Information)
                        self.msg.exec()             
                
    def SearchUpdate(self):
        if len(self.searchprofile_2.text()) != 0:
            db = sqlite3.connect('SIS.db')
            cur = db.cursor()
            cur.execute(f'SELECT * FROM students_information WHERE FullName = "{self.searchprofile_2.text()}"')
            GetInfo =cur.fetchall()
            validation = 0
            for info in GetInfo:
                validation += 1
                if os.path.isdir('imageHolder'):
                        shutil.rmtree('imageHolder')
                os.makedirs('imageHolder')
                
                with open('imageHolder/img.png', 'wb') as file:
                        file.write(info[0])
                self.ImageButton_2.setIcon(QtGui.QIcon('imageHolder/img.png'))
                
                self.updfname.setText(str(info[2]))
                self.updmname.setText(str(info[3]))
                self.updlname.setText(str(info[4]))
                self.updemail.setText(str(info[6]))
                self.updcourse.setCurrentText(str(info[7]))
                self.updaddress.setPlainText(str(info[8]))
                
                self.newdate = []
                if len(info[9]) == 8:
                        self.newdate.append(info[9][0])
                        self.newdate.append(info[9][2])
                        self.newdate.append(f'{info[9][4]}{info[9][5]}{info[9][6]}{info[9][7]}')
                        newyear = int(self.newdate[2])
                        newmonth = int(self.newdate[0])
                        newday = int(self.newdate[1])
                        self.updbirthdate.setDate(QtCore.QDate(newyear,newmonth,newday))
                elif len(info[9]) == 9 and info[9][1] == '/':
                        self.newdate.append(info[9][0])
                        self.newdate.append(f'{info[9][2]}{info[9][3]}')
                        self.newdate.append(f'{info[9][5]}{info[9][6]}{info[9][7]}{info[9][8]}')
                        newyear = int(self.newdate[2])
                        newmonth = int(self.newdate[0])
                        newday = int(self.newdate[1])
                        self.updbirthdate.setDate(QtCore.QDate(newyear,newmonth,newday))

                elif len(info[9]) == 9 and info[9][1] != '/':
                        self.newdate.append(f'{info[9][0]}{info[9][1]}')
                        self.newdate.append(f'{info[9][3]}')
                        self.newdate.append(f'{info[9][5]}{info[9][6]}{info[9][7]}{info[9][8]}')
                        newyear = int(self.newdate[2])
                        newmonth = int(self.newdate[0])
                        newday = int(self.newdate[1])
                        self.updbirthdate.setDate(QtCore.QDate(newyear,newmonth,newday))

                elif len(info[9]) > 8 and info[9][1] != '/':
                        self.newdate.append(f'{info[9][0]}{info[9][1]}')
                        self.newdate.append(f'{info[9][3]}{info[9][4]}')
                        self.newdate.append(f'{info[9][6]}{info[9][7]}{info[9][8]}{info[9][9]}')
                        newyear = int(self.newdate[2])
                        newmonth = int(self.newdate[0])
                        newday = int(self.newdate[1])
                        self.updbirthdate.setDate(QtCore.QDate(newyear,newmonth,newday))
                if len(info[9]) == 8:
                        self.newdate.append(info[9][0])
                        self.newdate.append(info[9][2])
                        self.newdate.append(f'{info[9][4]}{info[9][5]}{info[9][6]}{info[9][7]}')
                        newyear = int(self.newdate[2])
                        newmonth = int(self.newdate[0])
                        newday = int(self.newdate[1])
                        self.updbirthdate.setDate(QtCore.QDate(newyear,newmonth,newday))
                elif len(info[9]) == 9 and info[9][1] == '/':
                        self.newdate.append(info[9][0])
                        self.newdate.append(f'{info[9][2]}{info[9][3]}')
                        self.newdate.append(f'{info[9][5]}{info[9][6]}{info[9][7]}{info[9][8]}')
                        newyear = int(self.newdate[2])
                        newmonth = int(self.newdate[0])
                        newday = int(self.newdate[1])
                        self.updbirthdate.setDate(QtCore.QDate(newyear,newmonth,newday))

                elif len(info[9]) == 9 and info[9][1] != '/':
                        self.newdate.append(f'{info[9][0]}{info[9][1]}')
                        self.newdate.append(f'{info[9][3]}')
                        self.newdate.append(f'{info[9][5]}{info[9][6]}{info[9][7]}{info[9][8]}')
                        newyear = int(self.newdate[2])
                        newmonth = int(self.newdate[0])
                        newday = int(self.newdate[1])
                        self.updbirthdate.setDate(QtCore.QDate(newyear,newmonth,newday))

                elif len(info[9]) > 8 and info[9][1] != '/':
                        self.newdate.append(f'{info[9][0]}{info[9][1]}')
                        self.newdate.append(f'{info[9][3]}{info[9][4]}')
                        self.newdate.append(f'{info[9][6]}{info[9][7]}{info[9][8]}{info[9][9]}')
                        newyear = int(self.newdate[2])
                        newmonth = int(self.newdate[0])
                        newday = int(self.newdate[1])
                        self.updbirthdate.setDate(QtCore.QDate(newyear,newmonth,newday))


                self.updcontact.setText(f'0{str(info[10])}')
                self.updyear.setCurrentText(str(info[11]))
                self.updage.setText(str(info[12]))

                if info[13] == 'Male':
                        self.updmale.setChecked(True)
                if info[13] == 'Female':
                        self.updfemale.setChecked(True)

            if validation == 0:
                self.msg = QMessageBox()
                self.msg.setWindowIcon(QtGui.QIcon('images/students.png'))
                self.msg.setWindowTitle(' ')
                self.msg.setText('No record found.')
                self.msg.setIcon(QMessageBox.Icon.Information)
                self.msg.exec()

    def UpdateValidation(self):
        self.msg = QMessageBox()
        self.msg.setWindowIcon(QtGui.QIcon('images/students.png'))
        self.msg.setWindowTitle(' ')
        self.msg.setIcon(QMessageBox.Icon.Warning)
        self.msg.setText('Are you sure you want to update this student?')
        self.msg.setStandardButtons(QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.Cancel) 
        self.msg.buttonClicked.connect(self.Update_)    
        self.msg.exec() 

    def Update_(self, key):     
        if key.text() == '&Yes':
                InputList = [
                        self.updfname.text(),
                        self.updmname.text(),
                        self.updlname.text(),
                        self.updaddress.toPlainText(),
                        self.updage.text(),
                        self.updbirthdate.text(),
                        self.updcontact.text(),
                        self.updemail.text(),
                        self.updyear.currentIndex()
                        ]
                validation = 0
                for Input_ in InputList:
                        filterInput = str(Input_)
                        if len(filterInput) == 0:
                                validation += 1
                
                if validation == 0 and os.path.isdir('imageHolder'):
                        with open('imageHolder/img.png', 'rb') as file:
                                binaryData = file.read()

                                db = sqlite3.connect('SIS.db')
                                cur = db.cursor()
                                        
                                DateToday = datetime.datetime.now()
                                RegistrationDate = DateToday.strftime('%m/%d/%Y')

                                if self.updmale.isChecked():
                                        updgender = self.updmale.text()
                                        

                                if self.updfemale.isChecked():
                                        updgender = self.updfemale.text()
                                
                                self.updfullname = f'{self.updfname.text()} {self.updmname.text()} {self.updlname.text()}'
                                
                                cur.execute('UPDATE students_information SET \
                                        Profile = ?, FirstName = ?, MiddleName = ?, LastName = ?, Email = ?, FullName = ?, Course = ?, Address = ?, \
                                        Birthdate = ?, ContactNum = ?, YearLevel = ?, Age = ?, Gender = ? WHERE FullName = ?',

                                        (
                                                binaryData,
                                                self.updfname.text(),
                                                self.updmname.text(),
                                                self.updlname.text(),
                                                self.updemail.text(),
                                                self.updfullname,
                                                self.updcourse.currentText(),
                                                self.updaddress.toPlainText(),
                                                self.updbirthdate.text(),
                                                int(self.updcontact.text()),
                                                int(self.updyear.currentText()),
                                                int(self.updage.text()),
                                                updgender,
                                                self.searchprofile_2.text()
                                                )
                                        )

                                
                                db.commit()
                                self.searchprofile_2.clear()

                                self.msg = QMessageBox()
                                self.msg.setWindowIcon(QtGui.QIcon('images/students.png'))
                                self.msg.setWindowTitle(' ')
                                self.msg.setText('Student has been updated successfully.')
                                self.msg.setIcon(QMessageBox.Icon.Information)
                                self.msg.exec()

                                self.updaddress.clear()
                                self.updage.clear()
                                self.updbirthdate.setDate(QtCore.QDate(2000,1,1))
                                self.updcontact.clear()
                                self.updcourse.setCurrentIndex(0)
                                self.updemail.clear()
                                self.updfname.clear()
                                self.updmname.clear()
                                self.updlname.clear()
                                self.updyear.setCurrentIndex(0)
                                self.ImageButton_2.setIcon(QtGui.QIcon())

    def Register_(self):
        InputList = [
                self.regfname.text(),
                self.regmname.text(),
                self.reglname.text(),
                self.regaddress.toPlainText(),
                self.regage.text(),
                self.regbirthdate.text(),
                self.regcontact.text(),
                self.regemail.text(),
                self.regyear.currentIndex()
                ]
        validation = 0
        for Input_ in InputList:
                filterInput = str(Input_)
                if len(filterInput) == 0:
                        validation += 1
        
        if validation == 0 and os.path.isdir('imageHolder'):
                with open('imageHolder/img.png', 'rb') as file:
                        binaryData = file.read()

                        db = sqlite3.connect('SIS.db')
                        cur = db.cursor()
                                
                        DateToday = datetime.datetime.now()
                        RegistrationDate = DateToday.strftime('%m/%d/%Y')

                        if self.regmale.isChecked():
                                reggender = self.regmale.text()
                                

                        if self.regfemale.isChecked():
                                reggender = self.regfemale.text()
                        
                        self.fullname = f'{self.regfname.text()} {self.regmname.text()} {self.reglname.text()}'
                        
                        cur.execute('INSERT INTO students_information VALUES(?,NULL,?,?,?,?,?,?,?,?,?,?,?,?,?)',\
                        (binaryData,self.regfname.text(),self.regmname.text(),self.reglname.text(),self.fullname,self.regemail.text(),self.regcourse.currentText(),self.regaddress.toPlainText(),self.regbirthdate.text(),self.regcontact.text(),self.regyear.currentText(),self.regage.text(),reggender,RegistrationDate))
                        db.commit()

                        self.regaddress.clear()
                        self.regage.clear()
                        self.regbirthdate.setDate(QtCore.QDate(2000,1,1))
                        self.regcontact.clear()
                        self.regcourse.setCurrentIndex(0)
                        self.regemail.clear()
                        self.regfname.clear()
                        self.regmname.clear()
                        self.reglname.clear()
                        self.regyear.setCurrentIndex(0)
                        self.ImageButton.setIcon(QtGui.QIcon())

                        self.msg = QMessageBox()
                        self.msg.setWindowIcon(QtGui.QIcon('images/students.png'))
                        self.msg.setWindowTitle('')
                        self.msg.setText('Student has been added successfully.')
                        self.msg.setIcon(QMessageBox.Icon.Information)
                        self.msg.exec()

    def ViewListCourse(self):
        db = sqlite3.connect('SIS.db')
        cur = db.cursor()
        cur.execute(f'SELECT * FROM students_information WHERE Course = "{self.viewcoursecbox.currentText()}"')        
        Student = cur.fetchall()

        Students = []
        r = 1
        c = 0
        a = 0
        for item in Student:
                Students.append(item)
                c += 1
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(c+1)

        self.tableWidget.setItem(0,0,QtWidgets.QTableWidgetItem('Student ID'))  
        self.tableWidget.setItem(0,1,QtWidgets.QTableWidgetItem('Name'))  
        self.tableWidget.setItem(0,2,QtWidgets.QTableWidgetItem('Course'))  
        self.tableWidget.setItem(0,3,QtWidgets.QTableWidgetItem('Year'))  
        self.tableWidget.setItem(0,4,QtWidgets.QTableWidgetItem('Gender'))  
        self.tableWidget.setItem(0,5,QtWidgets.QTableWidgetItem('Contact No.'))  
        self.tableWidget.setItem(0,6,QtWidgets.QTableWidgetItem('Email'))  
        self.tableWidget.setItem(0,7,QtWidgets.QTableWidgetItem('Registration Date'))  


        for x in range(c):
                self.tableWidget.setItem(r,0,QtWidgets.QTableWidgetItem(str(Student[a][1])))
                self.tableWidget.setItem(r,1,QtWidgets.QTableWidgetItem(str(Student[a][5])))
                self.tableWidget.setItem(r,2,QtWidgets.QTableWidgetItem(str(Student[a][7])))
                self.tableWidget.setItem(r,3,QtWidgets.QTableWidgetItem(str(Student[a][11])))
                self.tableWidget.setItem(r,4,QtWidgets.QTableWidgetItem(str(Student[a][13])))
                self.tableWidget.setItem(r,5,QtWidgets.QTableWidgetItem(str(Student[a][10])))
                self.tableWidget.setItem(r,6,QtWidgets.QTableWidgetItem(str(Student[a][6])))
                self.tableWidget.setItem(r,7,QtWidgets.QTableWidgetItem(str(Student[a][14])))
                r = r + 1
                a = a + 1
        self.tableWidget.setFont(QtGui.QFont('Helvetica ', 7))
        self.tableWidget.setColumnWidth(0,60)
        self.tableWidget.setColumnWidth(1,125)
        self.tableWidget.setColumnWidth(2,130)
        self.tableWidget.setColumnWidth(3,20)
        self.tableWidget.setColumnWidth(4,40)
        self.tableWidget.setColumnWidth(5,60)
        self.tableWidget.setColumnWidth(6,130)
        self.tableWidget.setColumnWidth(7,60)

        self.tableWidget.horizontalHeader().hide()
        self.tableWidget.verticalHeader().hide()
        
        if c > 0:
                self.numberofstudents.setText(f'Total number of students: {c}')
        else:
                if self.viewcoursecbox.currentText() != ' Select course to view' and c == 0:
                        self.numberofstudents.setText(f'Total number of students: 0')
                        self.msg = QMessageBox()
                        self.msg.setWindowIcon(QtGui.QIcon('images/students.png'))
                        self.msg.setIcon(QMessageBox.Icon.Information)
                        self.msg.setWindowTitle(' ')
                        self.msg.setText('No record/s found.')
                        self.msg.exec()

    def ViewList(self):
        db = sqlite3.connect('SIS.db')
        cur = db.cursor()
        cur.execute('SELECT * FROM students_information')        
        Student = cur.fetchall()

        Students = []
        r = 1
        c = 0
        a = 0
        for item in Student:
                Students.append(item)
                c += 1
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(c+1)

        self.tableWidget.setItem(0,0,QtWidgets.QTableWidgetItem('Student ID'))  
        self.tableWidget.setItem(0,1,QtWidgets.QTableWidgetItem('Name'))  
        self.tableWidget.setItem(0,2,QtWidgets.QTableWidgetItem('Course'))  
        self.tableWidget.setItem(0,3,QtWidgets.QTableWidgetItem('Year'))  
        self.tableWidget.setItem(0,4,QtWidgets.QTableWidgetItem('Gender'))  
        self.tableWidget.setItem(0,5,QtWidgets.QTableWidgetItem('Contact No.'))  
        self.tableWidget.setItem(0,6,QtWidgets.QTableWidgetItem('Email'))  
        self.tableWidget.setItem(0,7,QtWidgets.QTableWidgetItem('Registration Date'))  


        for x in range(c):
                self.tableWidget.setItem(r,0,QtWidgets.QTableWidgetItem(str(Student[a][1])))
                self.tableWidget.setItem(r,1,QtWidgets.QTableWidgetItem(str(Student[a][5])))
                self.tableWidget.setItem(r,2,QtWidgets.QTableWidgetItem(str(Student[a][7])))
                self.tableWidget.setItem(r,3,QtWidgets.QTableWidgetItem(str(Student[a][11])))
                self.tableWidget.setItem(r,4,QtWidgets.QTableWidgetItem(str(Student[a][13])))
                self.tableWidget.setItem(r,5,QtWidgets.QTableWidgetItem(str(Student[a][10])))
                self.tableWidget.setItem(r,6,QtWidgets.QTableWidgetItem(str(Student[a][6])))
                self.tableWidget.setItem(r,7,QtWidgets.QTableWidgetItem(str(Student[a][14])))
                r = r + 1
                a = a + 1
        self.tableWidget.setFont(QtGui.QFont('Helvetica ', 7))
        self.tableWidget.setColumnWidth(0,60)
        self.tableWidget.setColumnWidth(1,125)
        self.tableWidget.setColumnWidth(2,130)
        self.tableWidget.setColumnWidth(3,20)
        self.tableWidget.setColumnWidth(4,40)
        self.tableWidget.setColumnWidth(5,60)
        self.tableWidget.setColumnWidth(6,130)
        self.tableWidget.setColumnWidth(7,60)

        self.tableWidget.horizontalHeader().hide()
        self.tableWidget.verticalHeader().hide()
        if c > 0:
                self.numberofstudents.setText(f'Total number of students: {c}')
        else:
                self.numberofstudents.setText(f'Total number of students: 0')

                self.msg = QMessageBox()
                self.msg.setWindowIcon(QtGui.QIcon('images/students.png'))
                self.msg.setWindowTitle(' ')
                self.msg.setIcon(QMessageBox.Icon.Information)
                self.msg.setText('No record/s found.')
                self.msg.exec()

    def AboutTheApp(self):
                self.about = QMessageBox()
                self.about.setWindowIcon(QtGui.QIcon('images/students.png'))
                self.about.setWindowTitle('Student Information System | About the app')
                self.about.setIcon(QMessageBox.Icon.Information)
                self.about.setText("Student Information System by Eli Bautista\n─────────────────────────────────────────────────────\nThis application is a platform that helps schools/colleges take student's information for easier management and helps them to communicate with the students via email.")
                self.about.show()

    def UploadImageRegister(self):
        if os.path.isdir('imageHolder'):
            shutil.rmtree('imageHolder')
        os.makedirs('imageHolder')
        FileName = QFileDialog.getOpenFileName(caption='Upload Image', filter='Image Files (*.jpg;*.png;*.jpeg;)')
        FilePath = FileName[0]
        if len(FilePath) != 0:
                with open(FilePath, 'rb') as file:
                        binaryData = file.read()

                with open('imageHolder/img.png', 'wb') as file:
                        file.write(binaryData)
                self.ImageButton.setIcon(QtGui.QIcon(FilePath))

    def UploadImageUpdate(self):
        if os.path.isdir('imageHolder'):
            shutil.rmtree('imageHolder')
        os.makedirs('imageHolder')
        FileName = QFileDialog.getOpenFileName(caption='Upload Image', filter='Image Files (*.jpg;*.png;*.jpeg;)')
        FilePath = FileName[0]
        if len(FilePath) != 0:
                with open(FilePath, 'rb') as file:
                        binaryData = file.read()

                with open('imageHolder/img.png', 'wb') as file:
                        file.write(binaryData)
                self.ImageButton_2.setIcon(QtGui.QIcon(FilePath))
    
    def ViewProfilePicture(self):

        if os.path.isdir('imageHolder'):
                if os.path.exists('imageHolder/img.png'): 
                        ImagePath = 'imageHolder/img.png'
                        ReadImage = cv2.imread(ImagePath)
                        ResizeImage = cv2.resize(ReadImage,(700,700))

                        WindowName = "Profile Picture"
                        cv2.namedWindow(WindowName)          # Create a named window
                        cv2.moveWindow(WindowName, 600,150)  # Move it to (600,150)
                        cv2.imshow(WindowName, ResizeImage)
                        
                        KeyPress = cv2.waitKey(0)
                        
                        if KeyPress == 27:
                                cv2.destroyAllWindows()

                if os.path.exists('imageHolder/img.jpg'): 
                        ImagePath = 'imageHolder/img.jpg'
                        ReadImage = cv2.imread(ImagePath)
                        ResizeImage = cv2.resize(ReadImage,(700,700))

                        WindowName = "Profile Picture"
                        cv2.namedWindow(WindowName)          # Create a named window
                        cv2.moveWindow(WindowName, 600,150)  # Move it to (600,150)
                        cv2.imshow(WindowName, ResizeImage)
                        
                        KeyPress = cv2.waitKey(0)
                        
                        if KeyPress == 27:
                                cv2.destroyAllWindows()

                if os.path.exists('imageHolder/img.jpeg'): 
                        ImagePath = 'imageHolder/img.jpeg'
                        ReadImage = cv2.imread(ImagePath)
                        ResizeImage = cv2.resize(ReadImage,(700,700))

                        WindowName = "Profile Picture"
                        cv2.namedWindow(WindowName)          # Create a named window
                        cv2.moveWindow(WindowName, 600,150)  # Move it to (600,150)
                        cv2.imshow(WindowName, ResizeImage)
                        
                        KeyPress = cv2.waitKey(0)
                        
                        if KeyPress == 27:
                                cv2.destroyAllWindows()

    def TakePictureUpdate(self):
        if os.path.isdir('imageHolder'):
                shutil.rmtree('imageHolder')
        os.makedirs('imageHolder')

        self.msgbox = QMessageBox()
        self.msgbox.setWindowTitle('')
        self.msgbox.setWindowIcon(QtGui.QIcon('images/students.png'))
        self.msgbox.setText('Press (s) to capture profile and (esc) to cancel.')
        self.msgbox.exec()

        CaptureVideo = cv2.VideoCapture(0)
        while True:
                ret, frame = CaptureVideo.read()
                if ret:
                        newFrame = cv2.resize(frame,(680,680))
                        mirrorFrame = cv2.flip(newFrame,1)
                        WindowName = "Take a picture"
                        cv2.namedWindow(WindowName)          # Create a named window
                        cv2.moveWindow(WindowName, 600,150)  # Move it to (600,150)
                        cv2.imshow(WindowName, mirrorFrame)

                        KeyPress = cv2.waitKey(1)

                        if KeyPress == 27:
                                break
                        elif KeyPress == ord('s'):
                                
                                cv2.imwrite('imageHolder/img.png',mirrorFrame)
                                self.ImageButton_2.setIcon(QtGui.QIcon('imageHolder/img.png'))
                                self.msgbox = QMessageBox()
                                self.msgbox.setWindowTitle('')
                                self.msgbox.setWindowIcon(QtGui.QIcon('images/students.png'))
                                self.msgbox.setText('Profile Captured.')
                                self.msgbox.exec()
                                break                                     

        cv2.destroyAllWindows()   
        CaptureVideo.release()

    def TakePictureRegister(self):
        if os.path.isdir('imageHolder'):
                shutil.rmtree('imageHolder')
        os.makedirs('imageHolder')

        self.msgbox = QMessageBox()
        self.msgbox.setWindowTitle('')
        self.msgbox.setWindowIcon(QtGui.QIcon('images/students.png'))
        self.msgbox.setText('Press (s) to capture profile and (esc) to cancel.')
        self.msgbox.exec()

        CaptureVideo = cv2.VideoCapture(0)
        while True:
                ret, frame = CaptureVideo.read()
                if ret:
                        newFrame = cv2.resize(frame,(680,680))
                        mirrorFrame = cv2.flip(newFrame,1)
                        WindowName = "Take a picture"
                        cv2.namedWindow(WindowName)          # Create a named window
                        cv2.moveWindow(WindowName, 600,150)  # Move it to (600,150)
                        cv2.imshow(WindowName, mirrorFrame)

                        KeyPress = cv2.waitKey(1)

                        if KeyPress == 27:
                                break
                        elif KeyPress == ord('s'):
                                
                                cv2.imwrite('imageHolder/img.png',mirrorFrame)
                                self.ImageButton.setIcon(QtGui.QIcon('imageHolder/img.png'))
                                self.msgbox = QMessageBox()
                                self.msgbox.setWindowTitle('')
                                self.msgbox.setWindowIcon(QtGui.QIcon('images/students.png'))
                                self.msgbox.setText('Profile Captured.')
                                self.msgbox.exec()
                                break

        cv2.destroyAllWindows()   
        CaptureVideo.release()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnAbout.setText(_translate("MainWindow", "About"))
        self.btnRegisterStudent.setText(_translate("MainWindow", "Register"))
        self.pushButton_7.setText(_translate("MainWindow", "x"))
        self.label_6.setText(_translate("MainWindow", "Register Student"))
        self.label_11.setText(_translate("MainWindow", "First Name"))
        self.label_12.setText(_translate("MainWindow", "Middle Name"))
        self.label_13.setText(_translate("MainWindow", "Last Name"))
        self.label_14.setText(_translate("MainWindow", "Course"))
        self.label_15.setText(_translate("MainWindow", "Year Level"))
        self.label_16.setText(_translate("MainWindow", "Age"))
        self.label_17.setText(_translate("MainWindow", "Email"))
        self.label_18.setText(_translate("MainWindow", "Contact No."))
        self.label_19.setText(_translate("MainWindow", "Address"))
        self.btnUploadProfile.setText(_translate("MainWindow", "Upload Profile"))
        self.btnTakePicture.setText(_translate("MainWindow", "Take a picture"))
        self.label_20.setText(_translate("MainWindow", "Date of Birth"))
        self.label_34.setText(_translate("MainWindow", "Gender"))
        self.regmale.setText(_translate("MainWindow", "Male"))
        self.regfemale.setText(_translate("MainWindow", "Female"))
        self.btnSaveChanges.setText(_translate("MainWindow", "Save"))
        self.pushButton_8.setText(_translate("MainWindow", "x"))
        self.label_8.setText(_translate("MainWindow", "Update Student"))
        self.label_21.setText(_translate("MainWindow", "First Name"))
        self.label_22.setText(_translate("MainWindow", "Middle Name"))
        self.label_23.setText(_translate("MainWindow", "Last Name"))
        self.label_24.setText(_translate("MainWindow", "Course"))
        self.label_25.setText(_translate("MainWindow", "Year Level"))
        self.label_26.setText(_translate("MainWindow", "Age"))
        self.label_27.setText(_translate("MainWindow", "Email"))
        self.label_28.setText(_translate("MainWindow", "Contact No."))
        self.label_29.setText(_translate("MainWindow", "Address"))
        self.btnUploadProfile_2.setText(_translate("MainWindow", "Upload Profile"))
        self.btnTakePicture_2.setText(_translate("MainWindow", "Take a picture"))
        self.label_30.setText(_translate("MainWindow", "Date of Birth"))
        self.label_40.setText(_translate("MainWindow", "Gender"))
        self.updmale.setText(_translate("MainWindow", "Male"))
        self.updfemale.setText(_translate("MainWindow", "Female"))
        self.btndeletestudent.setText(_translate("MainWindow", "Delete"))
        self.btnsearchprofile_2.setText(_translate("MainWindow", "Search"))
        self.searchprofile_2.setPlaceholderText(_translate("MainWindow", " Search student full name"))
        self.pushButton_9.setText(_translate("MainWindow", "x"))
        self.label_10.setText(_translate("MainWindow", "Student Records"))
        self.btndeleteallstudents.setText(_translate("MainWindow", "Delete All Students"))
        self.btnviewall.setText(_translate("MainWindow", "View All"))
        self.numberofstudents.setText(_translate("MainWindow", "Total no. of students : 0"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Student ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Gender"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Course"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Year"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Contact no"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Registration Date"))
        self.viewcoursecbox.setItemText(0, _translate("MainWindow", " Select course to view"))
        self.label_32.setText(_translate("MainWindow", "Student\'s Profile"))
        self.searchprofile.setPlaceholderText(_translate("MainWindow", " Search student full name"))
        self.btnsearchprofile.setText(_translate("MainWindow", "Search"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Student ID"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "First Name"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Middle Name"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Last Name"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Gender"))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Date of Birth"))
        item = self.tableWidget_2.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget_2.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "Contact No."))
        item = self.tableWidget_2.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "Course"))
        item = self.tableWidget_2.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "Year Level"))
        item = self.tableWidget_2.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "Address"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.btnsendemail.setText(_translate("MainWindow", "Send Email"))
        self.pushButton_11.setText(_translate("MainWindow", "x"))
        self.label_36.setText(_translate("MainWindow", "Send Email"))
        self.label_37.setText(_translate("MainWindow", "Subject:"))
        self.label_38.setText(_translate("MainWindow", "Message:"))
        self.label_39.setText(_translate("MainWindow", "To:"))
        self.btnsendemail_2.setText(_translate("MainWindow", "Send"))
        self.btnRegisterStudentPage.setText(_translate("MainWindow", "Register"))
        self.btnUpdateStudentPage.setText(_translate("MainWindow", "Update"))
        self.btnViewStudentpage.setText(_translate("MainWindow", "Student Records"))
        self.btnEmailStudentPage.setText(_translate("MainWindow", "Send Email"))
        self.btnViewStudentsProfilePage.setText(_translate("MainWindow", "View Profile"))
        self.btnHomePage.setText(_translate("MainWindow", "  STUDENT\n"
"             INFORMATION\n"
"SYSTEM"))
        self.btnExitApp.setText(_translate("MainWindow", "x"))
        self.label.setText(_translate("MainWindow", "Student Information System"))
        self.pushButton_6.setText(_translate("MainWindow", "x"))
        self.btnMinimizeApp.setText(_translate("MainWindow", "-"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
