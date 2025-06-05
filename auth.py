from PyQt6 import QtCore, QtGui, QtWidgets
import os


class Auth_Form(object):
    def setupUi(self, auth):
        auth.setObjectName("auth")
        auth.resize(500, 400)
        auth.setMaximumSize(QtCore.QSize(500, 400))

        icon_path = os.path.join(os.path.dirname(__file__), "images", "гор.PNG")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        auth.setWindowIcon(icon)

        background_label = QtWidgets.QLabel(parent=auth)
        background_label.setGeometry(0, 0, auth.width(), auth.height())
        background_path = os.path.join(os.path.dirname(__file__), "images", "IMG_3068.PNG")
        background_label.setPixmap(QtGui.QPixmap(background_path))
        background_label.setScaledContents(True)
        background_label.lower()

        self.frame = QtWidgets.QFrame(parent=auth)
        self.frame.setGeometry(QtCore.QRect(50, 50, 400, 300))
        self.frame.setStyleSheet("QFrame {\n"
                                 "    background-color: rgba(149, 140, 149, 75);"
                                 "border-radius: 15px; "
                                 "border: 2px solid #818181;\n"  # Полностью прозрачный
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        self.auth_2 = QtWidgets.QLabel(parent=self.frame)
        self.auth_2.setGeometry(QtCore.QRect(100, 80, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(16)
        self.auth_2.setFont(font)
        self.auth_2.setStyleSheet("color: #ffffff;")
        self.auth_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.auth_2.setObjectName("auth_2")

        self.label_icon = QtWidgets.QLabel(parent=self.frame)
        self.label_icon.setGeometry(QtCore.QRect(175, 20, 50, 50))
        self.label_icon.setText("")
        icon_path2 = os.path.join(os.path.dirname(__file__), "images", "гор строй-round-corners-round-corners (5).png")
        self.label_icon.setPixmap(QtGui.QPixmap(icon_path2))
        self.label_icon.setScaledContents(True)
        self.label_icon.setObjectName("label_icon")

        self.lineEdit_log = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_log.setGeometry(QtCore.QRect(50, 140, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        self.lineEdit_log.setFont(font)
        self.lineEdit_log.setStyleSheet("QLineEdit {\n"
                                        "    background-color: rgba(0, 0, 0, 120);\n"
                                        "    border: 1px solid #3c3c3c;\n"
                                        "    border-radius: 10px;\n"
                                        "    padding-left: 35px;\n"
                                        "    color: #ffffff;\n"
                                        "}\n"
                                        "QLineEdit:focus {\n"
                                        "    border: 2px solid #008080;\n"
                                        "}")
        self.lineEdit_log.setObjectName("lineEdit_log")

        self.icon_login = QtWidgets.QLabel(parent=self.frame)
        self.icon_login.setGeometry(QtCore.QRect(60, 145, 20, 20))
        self.icon_login.setText("")
        login_icon_path = os.path.join(os.path.dirname(__file__), "images", "login.PNG")
        self.icon_login.setPixmap(QtGui.QPixmap(login_icon_path))
        self.icon_login.setScaledContents(True)
        self.icon_login.setObjectName("icon_login")

        self.lineEdit_pass = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_pass.setGeometry(QtCore.QRect(50, 180, 300, 30))
        self.lineEdit_pass.setFont(font)
        self.lineEdit_pass.setStyleSheet("QLineEdit {\n"
                                         "    background-color: rgba(0, 0, 0, 120);\n"
                                         "    border: 1px solid #3c3c3c;\n"
                                         "    border-radius: 10px;\n""    padding-left: 35px;\n"
                                         "    color: #ffffff;\n"
                                         "}\n"
                                         "QLineEdit:focus {\n"
                                         "    border: 2px solid #008080;\n"
                                         "}")
        self.lineEdit_pass.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_pass.setObjectName("lineEdit_pass")

        self.icon_password = QtWidgets.QLabel(parent=self.frame)
        self.icon_password.setGeometry(QtCore.QRect(60, 185, 20, 20))
        self.icon_password.setText("")
        pass_icon_path = os.path.join(os.path.dirname(__file__), "images", "pass.PNG")
        self.icon_password.setPixmap(QtGui.QPixmap(pass_icon_path))
        self.icon_password.setScaledContents(True)
        self.icon_password.setObjectName("icon_password")

        self.pushButton_auth = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_auth.setGeometry(QtCore.QRect(50, 230, 300, 35))
        font.setPointSize(12)
        self.pushButton_auth.setFont(font)
        self.pushButton_auth.setStyleSheet("QPushButton {\n"
                                           "    background-color: rgba(7, 7, 7, 150);\n"
                                           "    color: white;\n"
                                           "    border-radius: 10px;\n"
                                           "    border: none;\n"
                                           "    padding: 5px;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgba(7, 7, 7, 180);\n"
                                           "}\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color: rgba(7, 7, 7, 200);\n"
                                           "}")
        button_icon_path = os.path.join(os.path.dirname(__file__), "images", "free-icon-log-in-3168040.png")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(button_icon_path), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_auth.setIcon(icon1)
        self.pushButton_auth.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_auth.setObjectName("pushButton_auth")

        self.label_copyright = QtWidgets.QLabel(parent=self.frame)
        self.label_copyright.setGeometry(QtCore.QRect(50, 280, 300, 20))
        font.setPointSize(8)
        self.label_copyright.setFont(font)
        self.label_copyright.setStyleSheet("color: #ffffff;")
        self.label_copyright.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_copyright.setObjectName("label_copyright")

        self.retranslateUi(auth)
        QtCore.QMetaObject.connectSlotsByName(auth)

    def retranslateUi(self, auth):
        _translate = QtCore.QCoreApplication.translate
        auth.setWindowTitle(_translate("auth", "Авторизация | ООО \"ГОР-СТРОЙ\""))
        self.auth_2.setText(_translate("auth", "АВТОРИЗАЦИЯ"))
        self.lineEdit_log.setPlaceholderText(_translate("auth", "Логин"))
        self.lineEdit_pass.setPlaceholderText(_translate("auth", "Пароль"))
        self.pushButton_auth.setText(_translate("auth", "ВОЙТИ"))
        self.label_copyright.setText(_translate("auth", "© 2025 ООО \"ГОР-СТРОЙ\". Все права защищены."))