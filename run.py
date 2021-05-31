from process import run
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.cb1 = QCheckBox('Show figure', self)
        self.cb2 = QCheckBox('Save figure', self)
        self.cb3 = QCheckBox('Save csv', self)
        self.cb1.move(20, 20)
        self.cb2.move(20, 60)
        self.cb3.move(20, 100)
        self.cb1.toggle()
        self.cb2.toggle()
        self.cb3.toggle()

        self.btnSave = QPushButton("set", self)
        self.btnSave.move(10, 160)
        self.btnSave.clicked.connect(self.btnInput_clicked)
        self.btnSave.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def btnInput_clicked(self):
        global show
        global save_fig
        global save_csv
        show = self.cb1.isChecked()
        save_fig = self.cb1.isChecked()
        save_csv = self.cb1.isChecked()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    app.exec_()
    print(show)
    print(save_fig)


run('.\data\**\*.xml',show ,save_fig,save_csv)

# run(path_file,show=False,save_fig=False,save_csv=False,file_input=None)

# 'Lot, Wafer, Mask, TestSite, Name, Date, Operator, Row, Column,
# error_flag, error_description, Analysis Wavelength, Rsq of Ref. spectrum,
# Rsq of IV, I at 1V[A], I at -1V[A]

# C:/Users/bluepc2020/PycharmProjects/project/project_lis2/data
# C:/data/P184640/**/*.xml
#C:/Users/blue2020/PycharmProjects/project_jot5/data/**/*.xml
# 'C:/data/P184640/D07/20190715_190855/**/*.xml'
# 'C:/data/P184640/D07/20190715_190855/**/*.xml'

# 'C:/data/P184640/D07/201900/**/*.xml'
