# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'discount_dialogue_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DiscountWindow(object):
    def setupUi(self, DiscountWindow):
        DiscountWindow.setObjectName("DiscountWindow")
        DiscountWindow.resize(453, 531)
        DiscountWindow.setStyleSheet("background-color:white;")
        self.centralwidget = QtWidgets.QWidget(DiscountWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget.setMinimumSize(QtCore.QSize(435, 487))
        self.verticalWidget.setMaximumSize(QtCore.QSize(435, 487))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalWidget1 = QtWidgets.QWidget(self.verticalWidget)
        self.verticalWidget1.setMinimumSize(QtCore.QSize(433, 428))
        self.verticalWidget1.setMaximumSize(QtCore.QSize(433, 428))
        self.verticalWidget1.setObjectName("verticalWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalWidget1)
        self.label.setMinimumSize(QtCore.QSize(431, 311))
        self.label.setMaximumSize(QtCore.QSize(431, 311))
        self.label.setStyleSheet("background-image: url(:/sign_in_dialogue/undraw_Happy_announcement_re_tsm0.png);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/discount/undraw_discount_d4bd.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.output_message = QtWidgets.QLabel(self.verticalWidget1)
        self.output_message.setMinimumSize(QtCore.QSize(400, 101))
        self.output_message.setMaximumSize(QtCore.QSize(400, 101))
        self.output_message.setStyleSheet("QLabel {\n"
"    font: 10pt \"Eras Medium ITC\";\n"
"    }")
        self.output_message.setWordWrap(True)
        self.output_message.setObjectName("output_message")
        self.gridLayout_2.addWidget(self.output_message, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout_2.addWidget(self.verticalWidget1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.ok = QtWidgets.QPushButton(self.verticalWidget)
        self.ok.clicked.connect(DiscountWindow.close)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok.sizePolicy().hasHeightForWidth())
        self.ok.setSizePolicy(sizePolicy)
        self.ok.setMinimumSize(QtCore.QSize(167, 49))
        self.ok.setMaximumSize(QtCore.QSize(167, 49))
        self.ok.setStyleSheet("QPushButton {\n"
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
        self.ok.setObjectName("ok")
        self.gridLayout.addWidget(self.ok, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.gridLayout_3.addWidget(self.verticalWidget, 0, 0, 1, 1)
        DiscountWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DiscountWindow)
        self.statusbar.setObjectName("statusbar")
        DiscountWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DiscountWindow)
        QtCore.QMetaObject.connectSlotsByName(DiscountWindow)

    def retranslateUi(self, DiscountWindow):
        _translate = QtCore.QCoreApplication.translate
        DiscountWindow.setWindowTitle(_translate("DiscountWindow", "MainWindow"))
        self.output_message.setText(_translate("DiscountWindow", "<html><head/><body><p align=\"center\">Get ready to save big! Use code RAYSTORE at checkout for 50% off your purchase .</p><p align=\"center\"><span style=\" font-weight:600; color:#4e47b8;\">Limited time only</span></p></body></html>"))
        self.ok.setText(_translate("DiscountWindow", "Ok"))
import qrc_img


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DiscountWindow = QtWidgets.QMainWindow()
    ui = Ui_DiscountWindow()
    ui.setupUi(DiscountWindow)
    DiscountWindow.show()
    sys.exit(app.exec_())