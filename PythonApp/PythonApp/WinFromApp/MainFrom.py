import sys
from Ui_WindowsFrom import MainWinFrom
from PyQt5.QtWidgets import QApplication, QMainWindow
from Update_Data import CreateHistoricalData
Ui_MainWindow =MainWinFrom.Ui_MainWindow

class MainFrom(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        #tt=CreateHistoricalData.CreateHistoricalData()
        #tt.Update_Stock_Data('000001','2017-01-01','2018-01-01','D')
        super(MainFrom, self).__init__(parent)
        self.setupUi(self)
