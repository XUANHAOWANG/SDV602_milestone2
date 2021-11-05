import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication
from UI_main import Ui_MainWindow
from upload import upload
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import matplotlib.pyplot as plt
import csv


class graph1(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(graph1, self).__init__(parent=None)
        self.setupUi(self)
        self.filename = 'White_shark_tagging_off_New_Zealand_between_April_2005_and_September_2009.csv'
        self.num = 0  # display 

        self.label.setStyleSheet('''QLabel{color:black;font-size:30px;font-family:Roman times;}''')  # 设置字体
        self.canvas = FigureCanvas(plt.figure(facecolor='#FFFFFF'))  # add canvel
        self.actionChoose_Data_Sourse.triggered.connect(self.dataSource)
        self.actionMerge_database.triggered.connect(self.slot1)
        self.actionExit.triggered.connect(QCoreApplication.instance().quit)
        self.nextButton.clicked.connect(self.next)
        self.previousButton.clicked.connect(self.previous)
        self.uploadButton.clicked.connect(self.slot1)
        self.updateButton.clicked.connect(self.slot2)
        self.exitButton.clicked.connect(QCoreApplication.instance().quit)
        # add verticalLayout
        self.mpl_ntb = NavigationToolbar(self.canvas, self)
        self.verticalLayout.addWidget(self.canvas)
        self.verticalLayout.addWidget(self.mpl_ntb)
        self.setLayout(self.verticalLayout)
        self.getdata(self.filename)
        self.Draw()

    def slot1(self):  # merge
        self.load = upload()
        self.load.signal.connect(self.getData_F2)  # path of file
        self.load.show()  # display merge layout

    def slot2(self):
        self.getdata(self.filename)  # data
        self.Draw() # draw

    def dataSource(self):
        self.filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Select csv datasource', '*.csv')
        self.slot2()

    def getData_F2(self, f):
        self.filename = f

    def next(self):
        self.num = (self.num + 1) % 3
        self.Draw()

    def previous(self):
        self.num = (self.num + 2) % 3
        self.Draw()

    def getdata(self, filename):
        
        self.mature = [0, 0, 0, 0]
        self.immature = [0, 0, 0, 0]
        self.cm300 = [0, 0, 0, 0]
        self.cm350 = [0, 0, 0, 0]
        self.cm400 = [0, 0, 0, 0]
        self.below400 = [0, 0, 0, 0]
        self.above440 = [0, 0, 0, 0]
        self.llatitude = []
        self.llongtitude = []
        self.gender = [0, 0]  # f, m
        self.num = 0

        plt.clf()
        dict = {'2005': 0, '2007': 1, '2008': 2, '2009': 3}
        with open(filename) as f:
            reader = csv.reader(f)
            head_row = next(reader)  # name
            for row in reader:
                # 读取坐标
                self.llatitude.append(float(row[21]))
                self.llongtitude.append(float(row[22]))
                # gender
                if row[16] == 'female':
                    self.gender[0] += 1
                elif row[16] == 'male':
                    self.gender[1] += 1
                # bar chart
                a = 0
                b = 0
                if row[19] != '2005' and row[19] != '2007' and row[19] != '2008' and row[19] != '2009':
                    continue
                if row[13][0] == 'M':
                    self.mature[dict[row[19]]] += 1
                elif row[13][0] == 'I':
                    self.immature[dict[row[19]]] += 1
                else:
                    continue
                # find cm
                for i in range(10, len(row[13])):
                    if row[13][i] == ' ':
                        if a == 0:
                            a = i + 1
                        else:
                            b = i
                    if b != 0:
                        break
                cm = row[13][a:b]

                if cm == '300':
                    self.cm300[dict[row[19]]] += 1
                elif cm == '350':
                    self.cm350[dict[row[19]]] += 1
                elif cm == '400':
                    self.cm400[dict[row[19]]] += 1
                elif '4' > cm[0] > '0':
                    self.below400[dict[row[19]]] += 1
                elif cm[0] == '4' and cm[1] >= '4' or cm == '420-450':
                    self.above440[dict[row[19]]] += 1

    def Draw(self):
        if self.num == 0:
            self.drawBar()
        elif self.num == 1:
            self.drawScatter()
        elif self.num == 2:
            self.drawPie()

    def drawBar(self):
        self.label.setText("White shark feature data")
        bar_width = 0.11  # 条形宽度
        t = ['2005', '2007', '2008', '2009']
        x = list(range(len(t)))
        plt.clf()
        plt.bar(x, self.mature, width=bar_width, label='Mature')
        plt.bar([i + bar_width for i in x], self.immature, width=bar_width, label='Immature')
        plt.bar([i + bar_width * 2 for i in x], self.cm300, width=bar_width, label='300 cm')
        plt.bar([i + bar_width * 3 for i in x], self.cm350, width=bar_width, label='350 cm')
        plt.bar([i + bar_width * 4 for i in x], self.cm400, width=bar_width, label='400 cm')
        plt.bar([i + bar_width * 5 for i in x], self.below400, width=bar_width, label='Below 400 cm')
        plt.bar([i + bar_width * 6 for i in x], self.above440, width=bar_width, label='Above 440 cm')
        plt.xticks([i + bar_width for i in x], t)  # 坐标填标签 t
        plt.legend()
        plt.xlabel('Year')
        w = 0
        for z in [self.mature, self.immature, self.cm300, self.cm350, self.cm400, self.below400, self.above440]:
            for xx, y in enumerate(z):
                plt.text(xx + w, y + 5, y, ha='center', fontsize=9)
            w += bar_width
        self.canvas.draw()  # 画图
        # self.canvas.flush_events()

    def drawPie(self):
        self.label.setText("White shark gender data")
        plt.clf()
        plt.pie(self.gender, labels=['female', 'male'], autopct='%1.2f%%')
        self.canvas.draw()
        # self.canvas.flush_events()

    def drawScatter(self):
        self.label.setText("White shark location data")
        plt.clf()
        # plt.plot(x, y, marker='o', ls='')
        plt.scatter(self.llongtitude, self.llatitude)
        plt.xlabel('Longtitude')
        plt.ylabel('Latitude')
        plt.title('New Zealand Location')
        plt.xlim(147, 181)  # x轴范围
        self.canvas.draw()
        # self.canvas.flush_events()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    x = graph1()
    x.show()
    sys.exit(app.exec_())