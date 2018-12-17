from Update_Data.BLL.Bll_PerformanceReport import PerformanceReport
class Bll_PerformanceReport():
    def __init__(self,parent=None):
        pass
    def Insert_Historical_Data(self,Year,Month):
        CreateTable=PerformanceReport()
        #if len(CreateTable.Select(Year=Year,Month=Month))==0:
        CreateTable.Create()
        CreateTable.Delete(Year=Year,Month=Month)
        CreateTable.INSERT(Year=Year,Month=Month)
