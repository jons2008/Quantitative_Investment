from Update_Data.DLL.HistoricalData.TodayTicks import TodayTicks
class Bll_TodayTicks():
    def __init__(self,parent=None):
        pass
    def Insert_Historical_Data(self,code,date):
        CreateTable=TodayTicks()
        CreateTable.Create(code=code)
        CreateTable.Delete(code=code,date=date)
        CreateTable.INSERT(code=code)
