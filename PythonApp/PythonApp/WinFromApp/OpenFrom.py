import sys
from Ui_WindowsFrom import OpenWindowsFrom
from PyQt5.QtWidgets import QApplication, QMainWindow
Ui_Child=OpenWindowsFrom.Ui_Form

class OpenFrom(QMainWindow,Ui_Child):
    def __init__(self):
        super(OpenFrom, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)
    def OPEN(self):
        self.show()