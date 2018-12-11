import sys
from Update_Data.HistoricalData.InsertHistoricalData import InsertHistoricalData
from Ui_WindowsFrom import MainWinFrom
from PyQt5.QtWidgets import QApplication, QMainWindow
Ui_MainWindow =MainWinFrom.Ui_MainWindow

class MainFrom(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        tt=InsertHistoricalData()
        tt.Insert_Historical_Data('000001','2017-01-1','2018-1-1','D')
        super(MainFrom, self).__init__(parent)
        self.setupUi(self)
