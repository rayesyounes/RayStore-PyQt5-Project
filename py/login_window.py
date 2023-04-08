# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):

    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(1192, 669)
        LoginWindow.setStyleSheet("background-color:white;")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.container = QtWidgets.QWidget(self.centralwidget)
        self.container.setObjectName("container")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.container)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.image_login = QtWidgets.QLabel(self.container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored,
                                           QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.image_login.sizePolicy().hasHeightForWidth())
        self.image_login.setSizePolicy(sizePolicy)
        self.image_login.setMinimumSize(QtCore.QSize(631, 471))
        self.image_login.setMaximumSize(QtCore.QSize(631, 471))
        self.image_login.setAcceptDrops(False)
        self.image_login.setAutoFillBackground(False)
        self.image_login.setStyleSheet(
            "background-image: url(:/login_img/undraw_Login_re_4vu2.png);\n"
            "\n"
            "")
        self.image_login.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.image_login.setText("")
        self.image_login.setTextFormat(QtCore.Qt.PlainText)
        self.image_login.setPixmap(
            QtGui.QPixmap(":/login/undraw_Login_re_4vu2.png"))
        self.image_login.setScaledContents(True)
        self.image_login.setAlignment(QtCore.Qt.AlignLeading
                                      | QtCore.Qt.AlignLeft
                                      | QtCore.Qt.AlignVCenter)
        self.image_login.setWordWrap(False)
        self.image_login.setOpenExternalLinks(False)
        self.image_login.setObjectName("image_login")
        self.horizontalLayout.addWidget(self.image_login)
        self.form = QtWidgets.QWidget(self.container)
        self.form.setMinimumSize(QtCore.QSize(421, 574))
        self.form.setMaximumSize(QtCore.QSize(421, 574))
        self.form.setStyleSheet("#form {\n"
                                "    background-color:#f2f2f2;\n"
                                "    border-style: solid;\n"
                                "    border-width: 2px;\n"
                                "    border-color:#6c63ff;\n"
                                "    border-radius: 60px;    \n"
                                "}")
        self.form.setObjectName("form")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.form)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.login_title = QtWidgets.QLabel(self.form)
        self.login_title.setMinimumSize(QtCore.QSize(421, 141))
        self.login_title.setMaximumSize(QtCore.QSize(421, 141))
        self.login_title.setStyleSheet(
            "QLabel {\n"
            "    background-color:#6c63ff;\n"
            "    font: 22pt \"Eras Medium ITC\";\n"
            "    color:white;\n"
            "\n"
            "    border-top-left-radius: 60px;    \n"
            "    border-top-right-radius: 60px;\n"
            "    }\n"
            "")
        self.login_title.setObjectName("login_title")
        self.gridLayout_2.addWidget(self.login_title, 0, 0, 1, 1)
        self.input_group = QtWidgets.QWidget(self.form)
        self.input_group.setObjectName("input_group")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.input_group)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.input_username = QtWidgets.QLineEdit(self.input_group)
        self.input_username.setMinimumSize(QtCore.QSize(400, 50))
        self.input_username.setMaximumSize(QtCore.QSize(400, 50))
        self.input_username.setStyleSheet(
            "QLineEdit {\n"
            "    padding-left:10px;\n"
            "    background-color:white;\n"
            "    font: 9pt \"Eras Medium ITC\";\n"
            "    color:2f2e41;\n"
            "    border-style: solid;\n"
            "    border-width: 2px;\n"
            "    border-radius: 10px;\n"
            "    border-color:#cccccc;\n"
            "\n"
            "    }\n"
            "\n"
            "QLineEdit:focus {\n"
            "    border-color:#2f2e41;\n"
            "    border-style:solid;\n"
            "}")
        self.input_username.setText("")
        self.input_username.setFrame(True)
        self.input_username.setCursorPosition(0)
        self.input_username.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.input_username.setObjectName("input_username")
        self.gridLayout_4.addWidget(self.input_username, 1, 0, 1, 1)
        self.output_message = QtWidgets.QLabel(self.input_group)
        self.output_message.setAlignment(QtCore.Qt.AlignCenter)
        self.output_message.setTextFormat(QtCore.Qt.RichText)
        self.output_message.setMinimumSize(QtCore.QSize(400, 50))
        self.output_message.setMaximumSize(QtCore.QSize(400, 50))
        self.output_message.setStyleSheet(
            "QLabel {\n"
            "    font: 10pt \"Eras Medium ITC\";\n"
            "    }")
        self.output_message.setObjectName("output_message")
        self.gridLayout_4.addWidget(self.output_message, 4, 0, 1, 1)
        self.input_password = QtWidgets.QLineEdit(self.input_group)
        self.input_password.setMinimumSize(QtCore.QSize(400, 50))
        self.input_password.setMaximumSize(QtCore.QSize(400, 50))
        self.input_password.setStyleSheet(
            "QLineEdit {\n"
            "        padding-left:10px;\n"
            "    background-color:white;\n"
            "    font: 9pt \"Eras Medium ITC\";\n"
            "    color:2f2e41;\n"
            "    border-style: solid;\n"
            "    border-width: 2px;\n"
            "    border-radius: 10px;\n"
            "    border-color:#cccccc;\n"
            "\n"
            "    }\n"
            "\n"
            "QLineEdit:focus {\n"
            "    border-color:#2f2e41;\n"
            "    border-style:solid;\n"
            "}")
        self.input_password.setInputMethodHints(QtCore.Qt.ImhNone)
        self.input_password.setText("")
        self.input_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.input_password.setMaxLength(16)
        self.input_password.setCursorPosition(0)
        self.input_password.setReadOnly(False)
        self.input_password.setObjectName("input_password")
        self.gridLayout_4.addWidget(self.input_password, 2, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.input_group)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 3, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.input_group)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_4.addWidget(self.line_2, 5, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.input_group)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_4.addWidget(self.line_3, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.input_group, 1, 0, 1, 1)
        self.button_group = QtWidgets.QWidget(self.form)
        self.button_group.setMinimumSize(QtCore.QSize(421, 81))
        self.button_group.setMaximumSize(QtCore.QSize(421, 81))
        self.button_group.setObjectName("button_group")
        self.gridLayout = QtWidgets.QGridLayout(self.button_group)
        self.gridLayout.setContentsMargins(1, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.back_home = QtWidgets.QPushButton(self.button_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.back_home.sizePolicy().hasHeightForWidth())

        self.back_home.clicked.connect(self.home_btn)
        self.back_home.clicked.connect(LoginWindow.close)

        self.back_home.setSizePolicy(sizePolicy)
        self.back_home.setMinimumSize(QtCore.QSize(166, 49))
        self.back_home.setMaximumSize(QtCore.QSize(166, 49))
        self.back_home.setStyleSheet("QPushButton {\n"
                                     "    background-color:#3f3d56;\n"
                                     "    font: 10pt \"Eras Medium ITC\";\n"
                                     "    color:white;\n"
                                     "    border-style:solid;\n"
                                     "    border-width: 3px;\n"
                                     "    border-radius: 20px;\n"
                                     "    border-color: beige;\n"
                                     "\n"
                                     "    }\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    background-color:#f2f2f2;\n"
                                     "    color:#3f3d56;\n"
                                     "    border-color:#3f3d56;\n"
                                     "    border-style: outset;\n"
                                     "    font-weight:bold;\n"
                                     "}")
        self.back_home.setAutoDefault(False)
        self.back_home.setDefault(False)
        self.back_home.setFlat(False)
        self.back_home.setObjectName("back_home")
        self.gridLayout.addWidget(self.back_home, 0, 3, 1, 1)
        self.log_in = QtWidgets.QPushButton(
            self.button_group, clicked=lambda: self.login_click(LoginWindow))

        # self.log_in.clicked.connect(self.login_click)
        # self.login_admin.clicked.connect(LoginWindow.close)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored,
                                           QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.log_in.sizePolicy().hasHeightForWidth())
        self.log_in.setSizePolicy(sizePolicy)
        self.log_in.setMinimumSize(QtCore.QSize(167, 49))
        self.log_in.setMaximumSize(QtCore.QSize(167, 49))
        self.log_in.setStyleSheet("QPushButton {\n"
                                  "    background-color:#564fcc;\n"
                                  "    font: 10pt \"Eras Medium ITC\";\n"
                                  "    color:white;\n"
                                  "    border-style: outset;\n"
                                  "    border-width: 3px;\n"
                                  "    border-radius: 20px;\n"
                                  "    border-color: beige;\n"
                                  "\n"
                                  "    }\n"
                                  "\n"
                                  "QPushButton:hover {\n"
                                  "    background-color:#f2f2f2;\n"
                                  "    color:#6c63ff;\n"
                                  "    border-color:#6c63ff;\n"
                                  "    border-style:outset;\n"
                                  "    font-weight:bold;\n"
                                  "}")
        self.log_in.setObjectName("log_in")
        self.gridLayout.addWidget(self.log_in, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.button_group, 2, 0, 1, 1)
        self.horizontalLayout.addWidget(self.form)
        self.verticalLayout_2.addWidget(self.container)
        LoginWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.login_title.setText(
            _translate(
                "LoginWindow",
                "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">LOGIN</span></p></body></html>"
            ))
        self.input_username.setPlaceholderText(
            _translate("LoginWindow", " Enter Username or email"))
        self.output_message.setText(
            _translate(
                "LoginWindow",
                "<html><head/><body><p align=\"center\">welcome to your favorite store</p></body></html>"
            ))
        self.input_password.setPlaceholderText(
            _translate("LoginWindow", " Enter Password"))
        self.back_home.setText(_translate("LoginWindow", "Back"))
        self.log_in.setText(_translate("LoginWindow", "Log in"))

    def home_btn(self):

        from main_window import Ui_MainWindow
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def login_click(self, LoginWindow):

        login = False

        with open('py/Client_File.txt') as file_client:

            lines = file_client.readlines()

        client_list = []

        for line in lines:

            client_list.append(line.strip())

        with open('py/Admin_File.txt') as file_admin:

            lines = file_admin.readlines()

        admin_list = []

        for line in lines:

            admin_list.append(line.strip())

        username = self.input_username.text()
        password = self.input_password.text()

        if username == "" or password == "":

            self.output_message.setText("please enter username and password")

        if username != "" and password != "":

            for combo in client_list:

                values = combo.strip().split(',')
                user_client_found = values[0]
                email_client_found = values[1]
                password_client_found = values[2]

                if user_client_found == username and password_client_found == password:

                    self.output_message.setText("successfull login client")
                    self.output_message.setStyleSheet("color: green")
                    self.save_cache()
                    self.input_username.setText("")
                    self.input_password.setText("")
                    self.login_client(LoginWindow)

                elif email_client_found == username and password_client_found == password:

                    self.output_message.setText("successfull login client")
                    self.output_message.setStyleSheet("color: green")
                    self.save_cache()
                    self.input_username.setText("")
                    self.input_password.setText("")
                    self.login_client(LoginWindow)

                elif user_client_found == username and password_client_found != password:

                    self.output_message.setText("incorrect password !")
                    self.output_message.setStyleSheet("color: red")

                elif email_client_found == username and password_client_found != password:

                    self.output_message.setText("incorrect password !")
                    self.output_message.setStyleSheet("color: red")

                elif (user_client_found and email_client_found
                      ) != username and password_client_found == password:

                    self.output_message.setText(
                        "Sorry, we couldn't find an account associated with that information. Please try again or create a new account"
                    )
                    self.output_message.setStyleSheet("color: black")

            for combo in admin_list:

                values = combo.strip().split(',')
                user_admin_found = values[0]
                email_admin_found = values[1]
                password_admin_found = values[2]

                if user_admin_found == username and password_admin_found == password:

                    self.output_message.setText("successfull login admin")
                    self.output_message.setStyleSheet("color: green")
                    self.input_username.setText("")
                    self.input_password.setText("")
                    self.login_admin(LoginWindow)

                elif email_admin_found == username and password_admin_found == password:

                    self.output_message.setText("successfull login admin")
                    self.output_message.setStyleSheet("color: green")
                    self.input_username.setText("")
                    self.input_password.setText("")
                    self.login_admin(LoginWindow)

                elif user_admin_found == username and password_admin_found != password:

                    self.output_message.setText("incorrect password !")
                    self.output_message.setStyleSheet("color: red")

                elif email_admin_found == username and password_admin_found != password:

                    self.output_message.setText("incorrect password !")
                    self.output_message.setStyleSheet("color: red")

                elif (user_admin_found and email_admin_found
                      ) != username and password_admin_found == password:

                    self.output_message.setText(
                        "Sorry, we couldn't find an account associated with that information. Please try again or create a new account"
                    )
                    self.output_message.setStyleSheet("color: black")

    def login_admin(self, LoginWindow):

        from product_window import Ui_ProductWindow
        self.ProductWindow = QtWidgets.QMainWindow()
        self.ui = Ui_ProductWindow()
        self.ui.setupUi(self.ProductWindow)
        self.ProductWindow.show()

        LoginWindow.close()

    def login_client(self, LoginWindow):

        from store_window import Ui_StoreWindow
        self.StoreWindow = QtWidgets.QMainWindow()
        self.ui = Ui_StoreWindow()
        self.ui.setupUi(self.StoreWindow)
        self.StoreWindow.show()

        LoginWindow.close()

    def save_cache(self):

        cache_list = []
        username = self.input_username.text()
        cache_line = username + "," + "product" + "," + "price per unite" + "," + "quantity" + "," + "payment methode" + "," + "total price"
        cache_list.append(cache_line)

        with open("py/Cache_File.txt", 'w') as cache:
            for item in cache_list:
                cache.write(item + '\n')


import qrc_img

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
