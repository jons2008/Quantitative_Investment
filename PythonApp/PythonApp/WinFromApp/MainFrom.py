import sys
from Update_Data.HistoricalData.InsertHistoricalData import InsertHistoricalData
from Ui_WindowsFrom import MainWinFrom
from PyQt5.QtWidgets import QApplication, QMainWindow
Ui_MainWindow =MainWinFrom.Ui_MainWindow
import tushare as ts
class MainFrom(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        #pro = ts.pro_api('5fb9fdc2747170d6eb5166b30ef6231ebbe32f5e27581fbb8feedc53')
        #
        ##查询当前所有正常上市交易的股票列表
        #
        #data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
        df = ts.get_stock_basics()
        tt=InsertHistoricalData()
        for stock in df.index:
            tt.Insert_Historical_Data(stock,'2005-01-01','2018-12-13','D')
            tt.Insert_Historical_Data(stock,'2005-01-01','2018-12-13','M')
            tt.Insert_Historical_Data(stock,'2005-01-01','2018-12-13','W')
            tt.Insert_Historical_Data(stock,'2018-01-01','2018-12-13','60')
            tt.Insert_Historical_Data(stock,'2018-01-01','2018-12-13','30')
            tt.Insert_Historical_Data(stock,'2018-01-01','2018-12-13','15')
            tt.Insert_Historical_Data(stock,'2018-08-01','2018-12-13','5')
        #for stock in df.index:
        #    tt.SET_Insert_TICK_DATA(stock)
        super(MainFrom, self).__init__(parent)
        self.setupUi(self)
