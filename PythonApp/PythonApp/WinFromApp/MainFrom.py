import sys
from Ui_WindowsFrom import MainWinFrom
from PyQt5.QtWidgets import QApplication, QMainWindow
Ui_MainWindow =MainWinFrom.Ui_MainWindow

class MainFrom(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainFrom, self).__init__(parent)
        self.setupUi(self)
