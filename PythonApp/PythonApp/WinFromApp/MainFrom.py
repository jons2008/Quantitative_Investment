import sys
from Update_Data.HistoricalData.InsertHistoricalData import InsertHistoricalData
from Ui_WindowsFrom import MainWinFrom
from PyQt5.QtWidgets import QApplication, QMainWindow
Ui_MainWindow =MainWinFrom.Ui_MainWindow
import tushare as ts
class MainFrom(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        df = ts.get_stock_basics()
        tt=InsertHistoricalData()
        for stock in df.index:
            tt.Insert_Historical_Data(stock,'2017-01-01','2018-01-01','D')
        super(MainFrom, self).__init__(parent)
        self.setupUi(self)
