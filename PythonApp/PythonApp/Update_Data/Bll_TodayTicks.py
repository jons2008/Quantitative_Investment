from Update_Data.HistoricalData.TodayTicks import TodayTicks


class Bll_TodayTicks():
    def __init__(self,parent=None):
        pass
    def Insert_Historical_Data(self,code,start,end,ktype):
        CreateTable=TodayTicks()
        CreateTable.Create(ktype=ktype,code=code)
        CreateTable.Delete(ktype=ktype,code=code,start=start,end=end)
        CreateTable.INSERT(code,start,end,ktype)
