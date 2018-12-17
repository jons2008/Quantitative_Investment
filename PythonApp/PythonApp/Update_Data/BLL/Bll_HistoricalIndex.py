
class Bll_HistoricalIndex():
    def __init__(self,parent=None):
        pass
    def Insert_Historical_Data(self,code,start,end):
        CreateTable=HistoricalIndex()
        if len(CreateTable.Select(time.strftime("%Y-%m-%d", time.localtime())))==0:
            CreateTable.Create()
            CreateTable.Delete(time.strftime("%Y-%m-%d", time.localtime()))
            CreateTable.INSERT()


