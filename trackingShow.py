import sys
from UI_tracking import Ui_WStracking
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from m3 import graph1


class WStracking(QtWidgets.QMainWindow, Ui_WStracking):
    def __init__(self):
        super(WStracking, self).__init__(parent=None)
        self.setupUi(self)
        self.g = graph1()

    def slot1(self):
        reply = QtWidgets.QMessageBox.information(self, "Welcome User", "Login successfully, Happy browsing!!")
        if reply == 1024:
            self.close()  # 关闭登陆界面
            self.g.show()  # 打开图形界面


if __name__ == '__main__':
    app = QApplication(sys.argv)
    x = WStracking()
    x.show()
    sys.exit(app.exec_())