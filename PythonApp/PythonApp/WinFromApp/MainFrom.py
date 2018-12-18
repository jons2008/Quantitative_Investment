import sys
from WinFromApp.View.View_TodayTicks import View_TodayTicks
from Update_Data.BLL.Bll_TodayTicks import Bll_TodayTicks
from Update_Data.BLL.Bll_HisData import Run_Bll_HisData
from Ui_WindowsFrom import MainWinFrom
from PyQt5.QtWidgets import QApplication, QMainWindow
Ui_MainWindow =MainWinFrom.Ui_MainWindow
import tushare as ts
import time
import threading
class MainFrom(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        #pro = ts.pro_api('5fb9fdc2747170d6eb5166b30ef6231ebbe32f5e27581fbb8feedc53')
        #
        ##查询当前所有正常上市交易的股票列表
        #
        #data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
        hitdata=View_TodayTicks()
        hitdata.Run()
        #df = ts.get_stock_basics()
        #for stock in df.index:
        #    hitdata.Insert_Historical_Data(stock,str(time.strftime("%Y-%m-%d", time.localtime()) ))
        #历史指数
        #bll=Bll_PerformanceReport()
        #bll.Insert_Historical_Data(2016,1)
        #bll.Insert_Historical_Data(2016,2)
        #bll.Insert_Historical_Data(2016,3)
        #bll.Insert_Historical_Data(2016,4)
        #bll.Insert_Historical_Data(2017,1)
        #bll.Insert_Historical_Data(2017,2)
        #bll.Insert_Historical_Data(2017,3)
        #bll.Insert_Historical_Data(2017,4)
        #bll.Insert_Historical_Data(2018,1)
        #bll.Insert_Historical_Data(2018,2)
        #bll.Insert_Historical_Data(2018,3)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #bll_todayticks=Bll_TodayTicks()
        #df = ts.get_stock_basics()
        #for stock in df.index:
        #    bll_todayticks.Insert_Historical_Data(stock,time.strftime("%Y-%m-%d", time.localtime()),time.strftime("%Y-%m-%d", time.localtime()))
        super(MainFrom, self).__init__(parent)
        self.setupUi(self)


