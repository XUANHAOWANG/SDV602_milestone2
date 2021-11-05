from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from UI_upload import Ui_Form
import csv


class upload(QtWidgets.QMainWindow, Ui_Form):
    signal = pyqtSignal(str)
    def __init__(self):
        super(upload, self).__init__(parent=None)
        self.setupUi(self)
        self.quitButton.clicked.connect(self.close)
        self.SButton.clicked.connect(self.slotS)
        self.TButton.clicked.connect(self.slotT)
        self.mergeButton.clicked.connect(self.slotM)

    def slotM(self, num):
        self.targetfile = self.TlineEdit.text()
        self.sourcefile = self.SlineEdit.text()
        if self.targetfile !='' and self.sourcefile != '':
            with open(self.sourcefile) as sf:
                reader = csv.reader(sf)
                head_row = next(reader)
                with open(self.targetfile, mode="a", newline="") as cfa:
                    wf = csv.writer(cfa)
                    for row in reader:
                        wf.writerow(row)  # 读一行写一行
            reply = QtWidgets.QMessageBox.information(self, "Merge success", "The file is merged and will be loaded for viewing.")
            if reply == 1024:  # 是ok
                self.signal.emit(self.targetfile)  # 发送信号量文件名
                self.close()

    def slotS(self):
        self.sfilename, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Select csv datasource', '*.csv')
        self.SlineEdit.setText(self.sfilename)

    def slotT(self):
        self.tfilename, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Select csv datasource', '*.csv')
        self.TlineEdit.setText(self.tfilename)
