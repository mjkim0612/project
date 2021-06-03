from process import run
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.cb1 = QCheckBox('Yes', self)
        self.cb4 = QCheckBox('No', self)

        self.cb2 = QCheckBox('Yes', self)
        self.cb5 = QCheckBox('No', self)

        self.cb3 = QCheckBox('Yes', self)
        self.cb6 = QCheckBox('No', self)

        self.cb7 = QCheckBox('External path', self)

        self.btnSave = QPushButton("set", self)
        self.btnSave.move(220, 180)
        self.btnSave.clicked.connect(self.btnInput_clicked)
        self.btnSave.clicked.connect(QCoreApplication.instance().quit)

        label1 = QLabel('Want to see the figure?',self)
        label1.move(20,20)
        self.cb1.move(20,40)
        self.cb4.move(70,40)

        label2 = QLabel('Want to save the figure?',self)
        label2.move(20,60)
        self.cb2.move(20,80)
        self.cb5.move(70,80)

        label3 = QLabel('Want to save the csv?',self)
        label3.move(20,100)
        self.cb3.move(20,120)
        self.cb6.move(70,120)
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        # label4 = QLabel('',self)
        # label4.move(20,140)
        self.cb7.move(20,140)

        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 400, 350, 220)

        self.le = QLineEdit('',self)
        self.le.move(140, 140)

        # label4 = QLabel('wafer',self)
        # label4.move(20, 160)
        # self.le2 = QLineEdit('',self)
        # self.le2.move(20, 180)

        self.show()

    def btnInput_clicked(self):
        global show
        global save_fig
        global save_csv
        global path_input
        global ex
        # global wafers

        show = self.cb1.isChecked()
        save_fig = self.cb5.isChecked()
        save_csv = self.cb6.isChecked()
        path_input = self.le.text()
        ex = self.cb7.isChecked()
        path_input = str(path_input)+'\\**\\*.xml'
        # wafers = False
        # if self.le.text() != None:
        #     wafers = self.le.text()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    app.exec_()
    # print(wafers)

run(ex,path_input,show,save_fig,save_csv)
# '.\data\**\*.xml'
# run(path_file,show=False,save_fig=False,save_csv=False,file_input=None)
# C:\Users\blue2020\OneDrive\바탕 화면\data
# 'Lot, Wafer, Mask, TestSite, Name, Date, Operator, Row, Column,
# error_flag, error_description, Analysis Wavelength, Rsq of Ref. spectrum,
# Rsq of IV, I at 1V[A], I at -1V[A]

# C:/Users/bluepc2020/PycharmProjects/project/project_lis2/data
# C:/data/P184640/**/*.xml
#C:/Users/blue2020/PycharmProjects/project_jot5/data/**/*.xml
# 'C:/data/P184640/D07/20190715_190855/**/*.xml'
# 'C:/data/P184640/D07/20190715_190855/**/*.xml'

# 'C:/data/P184640/D07/201900/**/*.xml'
