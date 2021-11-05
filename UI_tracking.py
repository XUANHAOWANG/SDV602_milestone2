from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QCoreApplication


class Ui_WStracking(object):
    def setupUi(self, WStracking):
        WStracking.setObjectName("WStracking")
        WStracking.setFixedSize(350, 300)
        self.centralwidget = QtWidgets.QWidget(WStracking)
        self.centralwidget.setObjectName("centralwidget")
        self.LoginButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoginButton.setGeometry(QtCore.QRect(60, 190, 100, 28))
        self.LoginButton.setObjectName("LoginButton")
        self.SignUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.SignUpButton.setGeometry(QtCore.QRect(200, 190, 100, 28))
        self.SignUpButton.setObjectName("SignUpButton")
        self.QuitButton = QtWidgets.QPushButton(self.centralwidget)
        self.QuitButton.setGeometry(QtCore.QRect(200, 240, 100, 28))
        self.QuitButton.setObjectName("QuitButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(135, 30, 80, 35))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label.setStyleSheet('''QLabel{color:blue;font-size:30px;font-family:Roman times;}''')
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 80, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 140, 80, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 90, 150, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 140, 150, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        WStracking.setCentralWidget(self.centralwidget)

        self.retranslateUi(WStracking)
        self.LoginButton.clicked.connect(WStracking.slot1)
        self.QuitButton.clicked.connect(QCoreApplication.instance().quit)
        #QtCore.QMetaObject.connectSlotsByName(WStracking)

    def retranslateUi(self, WStracking):
        _translate = QtCore.QCoreApplication.translate
        WStracking.setWindowTitle(_translate("WStracking", "White shark tracking"))
        self.LoginButton.setText(_translate("WStracking", "Login"))
        self.SignUpButton.setText(_translate("WStracking", "Sign Up"))
        self.QuitButton.setText(_translate("WStracking", "Quit"))
        self.label.setText(_translate("WStracking", "Login"))
        self.label_2.setText(_translate("WStracking", "Username"))
        self.label_3.setText(_translate("WStracking", "Password"))
