from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
import sqlite3, os, shutil



class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        LoginPage.setObjectName("LoginPage")
        LoginPage.resize(574, 391)
        self.frame_2 = QtWidgets.QFrame(LoginPage)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 571, 391))
        self.frame_2.setStyleSheet("QFrame{background-color:rgb(190, 0, 0);border:3px solid black}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(10, 40, 551, 341))
        self.frame.setStyleSheet("background-color:rgb(57, 57, 57)")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.btnAbout = QtWidgets.QPushButton(self.frame)
        self.btnAbout.setGeometry(QtCore.QRect(10, 480, 71, 28))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btnAbout.setFont(font)
        self.btnAbout.setStyleSheet("color:white;border-radius:1px")
        self.btnAbout.setFlat(True)
        self.btnAbout.setObjectName("btnAbout")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(243, 70, 70, 70))
        self.label_3.setStyleSheet("border:none")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("images/students.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(5, 131, 543, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border:none;color:white")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.username = QtWidgets.QLineEdit(self.frame)
        self.username.setGeometry(QtCore.QRect(163, 170, 251, 31))
        self.username.setStyleSheet("border:1px solid black;background-color:white;color:black;padding:5px")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(163, 210, 251, 31))
        self.password.setStyleSheet("border:1px solid black;background-color:white;color:black;padding:5px")
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password.setObjectName("password")
        self.btnlogin = QtWidgets.QPushButton(self.frame)
        self.btnlogin.setGeometry(QtCore.QRect(420, 210, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnlogin.setFont(font)
        self.btnlogin.setStyleSheet("background:rgb(57, 57, 57)")
        self.btnlogin.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/login.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnlogin.setIcon(icon)
        self.btnlogin.setDefault(False)
        self.btnlogin.setFlat(False)
        self.btnlogin.setObjectName("btnlogin")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(125, 170, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border:none;background-color:rgb(255, 214, 8)\n"
"")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("images/user.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(125, 210, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border:none;background-color:rgb(255, 214, 8)\n"
"")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("images/blacklock.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")
        self.btnTogglePassword = QtWidgets.QPushButton(self.frame)
        self.btnTogglePassword.setGeometry(QtCore.QRect(385, 210, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnTogglePassword.setFont(font)
        self.btnTogglePassword.setStyleSheet("border:1px solid black;background-color:white;color:black;border-width: 1px 0px 1px 0px;")
        self.btnTogglePassword.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/hidepw.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnTogglePassword.setIcon(icon1)
        self.btnTogglePassword.setCheckable(True)
        self.btnTogglePassword.setFlat(False)
        self.btnTogglePassword.setObjectName("btnTogglePassword")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 551, 31))
        self.frame_3.setStyleSheet("background-color:rgb(26, 26, 26)")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.btnExitApp = QtWidgets.QPushButton(self.frame_3)
        self.btnExitApp.setGeometry(QtCore.QRect(520, 0, 31, 28))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnExitApp.setFont(font)
        self.btnExitApp.setStyleSheet("color:white;border-width: 1px 0px 1px\n"
"")
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
        self.label_2.setStyleSheet("border:none\n"
"")
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
        self.btnMinimizeApp.setGeometry(QtCore.QRect(490, 0, 31, 28))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnMinimizeApp.setFont(font)
        self.btnMinimizeApp.setStyleSheet("color:white;border-width: 1px 0px 1px\n"
"")
        self.btnMinimizeApp.setFlat(True)
        self.btnMinimizeApp.setObjectName("btnMinimizeApp")

        self.retranslateUi(LoginPage)
        QtCore.QMetaObject.connectSlotsByName(LoginPage)

        self.Commit()

    def Commit(self):
        self.CreateDatabase()
        LoginPage.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        LoginPage.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.btnExitApp.clicked.connect(lambda:LoginPage.close())
        self.btnMinimizeApp.clicked.connect(lambda:LoginPage.showMinimized())
        self.password.returnPressed.connect(self.CheckAccount)
        self.btnlogin.clicked.connect(self.CheckAccount)
        self.btnTogglePassword.toggled.connect(self.TogglePassword)


    def CreateDatabase(self):
        if os.path.exists('SIS.db') is False:
            db = sqlite3.connect('SIS.db')
            cur = db.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS students_information
                (
                Profile BLOB,
                StudentID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                FirstName TEXT NOT NULL,
                MiddleName TEXT NOT NULL,
                LastName TEXT NOT NULL,
                FullName TEXT NOT NULL,
                Email TEXT,
                Course TEXT,
                Address TEXT,
                Birthdate TEXT,
                ContactNum BIGINT,
                YearLevel INT,
                Age INT,
                Gender TEXT,
                RegistrationDate TEXT
                )
                ''')
            cur.execute('UPDATE sqlite_sequence SET seq = 1000')
            db.commit()

    def TogglePassword(self):
        if self.btnTogglePassword.isChecked():
            self.btnTogglePassword.setIcon(QtGui.QIcon('images/showpw.png'))
            self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:
            self.btnTogglePassword.setIcon(QtGui.QIcon('images/hidepw.png'))
            self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def CheckAccount(self):
        username_input = self.username.text()
        password_input = self.password.text()
        valid_username = 'admin'
        valid_password = '1234'
        if username_input == valid_username and password_input == valid_password:
            
            self.username.clear()
            self.password.clear()

            from MainWindow import Ui_MainWindow
            self.mainwindow = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.mainwindow)
            self.ui.btnExitApp.clicked.connect(lambda:self.mainwindow.close())
            self.ui.btnMinimizeApp.clicked.connect(lambda:self.mainwindow.showMinimized())
            if os.path.exists('imageHolder'):
                    self.ui.btnExitApp.clicked.connect(lambda:shutil.rmtree('imageHolder'))
            self.mainwindow.show()

        else:
            self.msg = QMessageBox()
            self.msg.setWindowIcon(QtGui.QIcon('images/students.png'))
            self.msg.setWindowTitle('Admin Login')
            self.msg.setIcon(QMessageBox.Icon.Warning)
            self.msg.setText('Incorrect username / password.')
            self.msg.setInformativeText('Please try again.')
            self.msg.exec()




    def retranslateUi(self, LoginPage):
        _translate = QtCore.QCoreApplication.translate
        LoginPage.setWindowTitle(_translate("LoginPage", "LoginPage"))
        self.btnAbout.setText(_translate("LoginPage", "About"))
        self.label_4.setText(_translate("LoginPage", "Student Information System"))
        self.username.setPlaceholderText(_translate("LoginPage", " Username"))
        self.password.setPlaceholderText(_translate("LoginPage", " Password"))
        self.btnExitApp.setText(_translate("LoginPage", "x"))
        self.label.setText(_translate("LoginPage", "Student Information System"))
        self.pushButton_6.setText(_translate("LoginPage", "x"))
        self.btnMinimizeApp.setText(_translate("LoginPage", "-"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginPage = QtWidgets.QWidget()
    ui = Ui_LoginPage()
    ui.setupUi(LoginPage)
    LoginPage.show()
    sys.exit(app.exec())
