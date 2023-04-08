# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transaction_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_transaction_window(object):

    def setupUi(self, transaction_window):
        transaction_window.setObjectName("transaction_window")
        transaction_window.resize(997, 615)
        transaction_window.setStyleSheet("background-color:white;")
        self.centralwidget = QtWidgets.QWidget(transaction_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(541, 451))
        self.label.setMaximumSize(QtCore.QSize(541, 451))
        self.label.setText("")
        self.label.setPixmap(
            QtGui.QPixmap(
                ":/transaction/undraw_Happy_announcement_re_tsm0.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget_4.setMinimumSize(QtCore.QSize(411, 108))
        self.verticalWidget_4.setMaximumSize(QtCore.QSize(411, 108))
        self.verticalWidget_4.setObjectName("verticalWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalWidget_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.verticalWidget_4)
        self.label_7.setMinimumSize(QtCore.QSize(161, 50))
        self.label_7.setMaximumSize(QtCore.QSize(161, 50))
        self.label_7.setStyleSheet("\n"
                                   "    font: 12pt \"Eras Medium ITC\";")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.username = QtWidgets.QTextBrowser(self.verticalWidget_4)
        self.username.setMinimumSize(QtCore.QSize(400, 50))
        self.username.setMaximumSize(QtCore.QSize(400, 50))
        self.username.setAutoFillBackground(False)
        self.username.setStyleSheet("\n"
                                    "    padding-left:10px;\n"
                                    "    background-color:white;\n"
                                    "    font: 12pt \"Eras Medium ITC\";\n"
                                    "    color:2f2e41;\n"
                                    "    border-style: solid;\n"
                                    "    border-width: 2px;\n"
                                    "    border-radius: 10px;\n"
                                    "    border-color:#cccccc;\n"
                                    "\n"
                                    "\n"
                                    "    border-style:solid;\n"
                                    "")
        self.username.setInputMethodHints(QtCore.Qt.ImhNone)
        self.username.setLineWidth(1)
        self.username.setAutoFormatting(QtWidgets.QTextEdit.AutoBulletList)
        self.username.setTabChangesFocus(False)
        self.username.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.username.setLineWrapColumnOrWidth(0)
        self.username.setMarkdown("")
        self.username.setObjectName("username")
        self.verticalLayout_4.addWidget(self.username)
        self.verticalLayout.addWidget(self.verticalWidget_4)
        self.verticalWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget_5.setMinimumSize(QtCore.QSize(411, 108))
        self.verticalWidget_5.setMaximumSize(QtCore.QSize(411, 108))
        self.verticalWidget_5.setObjectName("verticalWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalWidget_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.verticalWidget_5)
        self.label_8.setMinimumSize(QtCore.QSize(161, 50))
        self.label_8.setMaximumSize(QtCore.QSize(161, 50))
        self.label_8.setStyleSheet("\n"
                                   "    font: 12pt \"Eras Medium ITC\";")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.Product_name = QtWidgets.QTextBrowser(self.verticalWidget_5)
        self.Product_name.setMinimumSize(QtCore.QSize(400, 50))
        self.Product_name.setMaximumSize(QtCore.QSize(400, 50))
        self.Product_name.setAutoFillBackground(False)
        self.Product_name.setStyleSheet("\n"
                                        "    padding-left:10px;\n"
                                        "    background-color:white;\n"
                                        "    font: 12pt \"Eras Medium ITC\";\n"
                                        "    color:2f2e41;\n"
                                        "    border-style: solid;\n"
                                        "    border-width: 2px;\n"
                                        "    border-radius: 10px;\n"
                                        "    border-color:#cccccc;\n"
                                        "\n"
                                        "\n"
                                        "    border-style:solid;\n"
                                        "")
        self.Product_name.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Product_name.setLineWidth(1)
        self.Product_name.setAutoFormatting(QtWidgets.QTextEdit.AutoBulletList)
        self.Product_name.setTabChangesFocus(False)
        self.Product_name.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.Product_name.setLineWrapColumnOrWidth(0)
        self.Product_name.setMarkdown("")
        self.Product_name.setObjectName("Product_name")
        self.verticalLayout_5.addWidget(self.Product_name)
        self.verticalLayout.addWidget(self.verticalWidget_5)
        self.verticalWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget_7.setMinimumSize(QtCore.QSize(411, 108))
        self.verticalWidget_7.setMaximumSize(QtCore.QSize(411, 108))
        self.verticalWidget_7.setObjectName("verticalWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalWidget_7)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.verticalWidget_7)
        self.label_10.setMinimumSize(QtCore.QSize(393, 34))
        self.label_10.setMaximumSize(QtCore.QSize(393, 34))
        self.label_10.setStyleSheet("\n"
                                    "    font: 12pt \"Eras Medium ITC\";")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_7.addWidget(self.label_10)
        self.payment_methode = QtWidgets.QTextBrowser(self.verticalWidget_7)
        self.payment_methode.setMinimumSize(QtCore.QSize(400, 50))
        self.payment_methode.setMaximumSize(QtCore.QSize(400, 50))
        self.payment_methode.setAutoFillBackground(False)
        self.payment_methode.setStyleSheet(
            "\n"
            "    padding-left:10px;\n"
            "    background-color:white;\n"
            "    font: 12pt \"Eras Medium ITC\";\n"
            "    color:2f2e41;\n"
            "    border-style: solid;\n"
            "    border-width: 2px;\n"
            "    border-radius: 10px;\n"
            "    border-color:#cccccc;\n"
            "\n"
            "\n"
            "    border-style:solid;\n"
            "")
        self.payment_methode.setInputMethodHints(QtCore.Qt.ImhNone)
        self.payment_methode.setLineWidth(1)
        self.payment_methode.setAutoFormatting(
            QtWidgets.QTextEdit.AutoBulletList)
        self.payment_methode.setTabChangesFocus(False)
        self.payment_methode.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.payment_methode.setLineWrapColumnOrWidth(0)
        self.payment_methode.setMarkdown("")
        self.payment_methode.setObjectName("payment_methode")
        self.verticalLayout_7.addWidget(self.payment_methode)
        self.verticalLayout.addWidget(self.verticalWidget_7)
        self.verticalWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget_6.setMinimumSize(QtCore.QSize(411, 108))
        self.verticalWidget_6.setMaximumSize(QtCore.QSize(411, 108))
        self.verticalWidget_6.setObjectName("verticalWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalWidget_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.verticalWidget_6)
        self.label_9.setMinimumSize(QtCore.QSize(161, 50))
        self.label_9.setMaximumSize(QtCore.QSize(161, 50))
        self.label_9.setStyleSheet("\n"
                                   "    font: 12pt \"Eras Medium ITC\";")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self.total_price = QtWidgets.QTextBrowser(self.verticalWidget_6)
        self.total_price.setMinimumSize(QtCore.QSize(400, 50))
        self.total_price.setMaximumSize(QtCore.QSize(400, 50))
        self.total_price.setAutoFillBackground(False)
        self.total_price.setStyleSheet("\n"
                                       "    padding-left:10px;\n"
                                       "    background-color:white;\n"
                                       "    font: 12pt \"Eras Medium ITC\";\n"
                                       "    color:2f2e41;\n"
                                       "    border-style: solid;\n"
                                       "    border-width: 2px;\n"
                                       "    border-radius: 10px;\n"
                                       "    border-color:#cccccc;\n"
                                       "\n"
                                       "\n"
                                       "    border-style:solid;\n"
                                       "")
        self.total_price.setInputMethodHints(QtCore.Qt.ImhNone)
        self.total_price.setLineWidth(1)
        self.total_price.setAutoFormatting(QtWidgets.QTextEdit.AutoBulletList)
        self.total_price.setTabChangesFocus(False)
        self.total_price.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.total_price.setLineWrapColumnOrWidth(0)
        self.total_price.setMarkdown("")
        self.total_price.setObjectName("total_price")
        self.verticalLayout_6.addWidget(self.total_price)
        self.verticalLayout.addWidget(self.verticalWidget_6)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ok = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.ok_click(transaction_window))
        self.ok.clicked.connect(transaction_window.close)
        self.ok.setMinimumSize(QtCore.QSize(171, 41))
        self.ok.setMaximumSize(QtCore.QSize(171, 41))
        self.ok.setStyleSheet("QPushButton {\n"
                              "    background-color:#f9f9f9;\n"
                              "    font: 10pt \"Eras Medium ITC\";\n"
                              "    color:#6c63ff;\n"
                              "    border-style: outset;\n"
                              "    border-width: 3px;\n"
                              "    border-radius: 20px;\n"
                              "    font-weight:bold;\n"
                              "    border-color:#6c63ff;\n"
                              "\n"
                              "    }\n"
                              "\n"
                              "QPushButton:hover {\n"
                              "    background-color:#6c63ff;\n"
                              "    color:#f9f9f9;\n"
                              "    border-color:#6c63ff;\n"
                              "    border-style:solide;\n"
                              "    font-weight:bold;\n"
                              "}")
        self.ok.setObjectName("ok")
        self.horizontalLayout.addWidget(self.ok)
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.clicked.connect(self.cancel_click)
        self.cancel.setMinimumSize(QtCore.QSize(171, 41))
        self.cancel.setMaximumSize(QtCore.QSize(171, 41))
        self.cancel.setStyleSheet("QPushButton {\n"
                                  "    background-color:#f9f9f9;\n"
                                  "    font: 10pt \"Eras Medium ITC\";\n"
                                  "    color:#6c63ff;\n"
                                  "    border-style: outset;\n"
                                  "    border-width: 3px;\n"
                                  "    border-radius: 20px;\n"
                                  "    font-weight:bold;\n"
                                  "    border-color:#6c63ff;\n"
                                  "\n"
                                  "    }\n"
                                  "\n"
                                  "QPushButton:hover {\n"
                                  "    background-color:#6c63ff;\n"
                                  "    color:#f9f9f9;\n"
                                  "    border-color:#6c63ff;\n"
                                  "    border-style:solide;\n"
                                  "    font-weight:bold;\n"
                                  "}")
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 23,
                                           QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        transaction_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(transaction_window)
        QtCore.QMetaObject.connectSlotsByName(transaction_window)

    def retranslateUi(self, transaction_window):
        _translate = QtCore.QCoreApplication.translate
        transaction_window.setWindowTitle(
            _translate("transaction_window", "MainWindow"))
        self.label_7.setText(_translate("transaction_window", "Username"))
        self.username.setHtml(
            _translate(
                "transaction_window",
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Eras Medium ITC\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\"-qt-paragraph-type:empty; margin-top:8px; margin-bottom:8px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"
            ))
        self.label_8.setText(_translate("transaction_window",
                                        "Product name :"))
        self.Product_name.setHtml(
            _translate(
                "transaction_window",
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Eras Medium ITC\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\"-qt-paragraph-type:empty; margin-top:8px; margin-bottom:8px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"
            ))
        self.label_10.setText(
            _translate("transaction_window", "Payment methode"))
        self.payment_methode.setHtml(
            _translate(
                "transaction_window",
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Eras Medium ITC\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\"-qt-paragraph-type:empty; margin-top:8px; margin-bottom:8px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"
            ))
        self.label_9.setText(_translate("transaction_window", "Totale price"))
        self.total_price.setHtml(
            _translate(
                "transaction_window",
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Eras Medium ITC\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\"-qt-paragraph-type:empty; margin-top:8px; margin-bottom:8px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"
            ))
        self.ok.setText(_translate("transaction_window", "ok"))
        self.cancel.setText(_translate("transaction_window", "cancel"))
        self.fill_info()

    def fill_info(self):

        with open("py/Cache_File.txt", "r") as cache_file:

            lines = cache_file.readlines()

        cache_list = []

        for line in lines:

            cache_list.append(line.strip())

        for combo in cache_list:

            values = combo.strip().split(',')
            username = values[0]
            product = values[1]
            price_per_unite = values[2]
            quantity = values[3]
            payment_methode = values[4]
            total = values[5]

        self.username.setText(username)
        self.Product_name.setText(product)
        self.payment_methode.setText(payment_methode)
        self.total_price.setText(total)

    def ok_click(self, transaction_window):

        from payment_dialogue_window import Ui_Payment_dialogue_Window
        self.Payment_dialogue_Window = QtWidgets.QMainWindow()
        self.ui = Ui_Payment_dialogue_Window()
        self.ui.setupUi(self.Payment_dialogue_Window)
        self.Payment_dialogue_Window.show()

        with open('py/selles_file.txt') as selles:

            lines = selles.readlines()

        selles_list = []

        for line in lines:

            selles_list.append(line.strip())

        with open("py/Cache_File.txt", "r") as cache_file:

            lines = cache_file.readlines()

        cache_list = []

        for line in lines:

            cache_list.append(line.strip())

        for combo in cache_list:

            values = combo.strip().split(',')
            username = values[0]
            product = values[1]
            price_per_unite = values[2]
            quantity = values[3]
            payment_methode = values[4]
            total = values[5]

            selles_line = username + "-" + product + "-" + price_per_unite + "-" + quantity + "-" + total + "-" + payment_methode

            selles_list.append(selles_line)

        with open('py/selles_file.txt', 'w') as file_selles:

            for item in selles_list:

                file_selles.write(item + '\n')

        transaction_window.close()

    def cancel_click(self):

        from payment_window import Ui_PaymentWindow
        self.PaymentWindow = QtWidgets.QMainWindow()
        self.ui = Ui_PaymentWindow()
        self.ui.setupUi(self.PaymentWindow)
        self.PaymentWindow.show()


import qrc_img

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    transaction_window = QtWidgets.QMainWindow()
    ui = Ui_transaction_window()
    ui.setupUi(transaction_window)
    transaction_window.show()
    sys.exit(app.exec_())