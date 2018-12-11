import tushare as ts
from Update_Data.HistoricalData import DeleteHistoricaData
from Update_Data.HistoricalData.CreateHistoricalData import CreateHistoricalData
from sqlalchemy import create_engine 

class InsertHistoricalData():

    def __init__(self,parent=None):
        pass
    def Insert_Historical_Data(self,code,start,end,ktype,retry_count=3,pause=0):
        
        CreateTable=CreateHistoricalData()

        CreateTable.CREATE_TABLE(ktype,code)
        DelTable=DeleteHistoricaData.DeleteHistoricaData()
        DelTable.Delete_TABLE(ktype,code,start,end)
        self.INSERT_TABLE(code,start,end,ktype)
    #添加数据进入表中
    def INSERT_TABLE(self,code,start,end,ktype):
         switcher = {
            'D':self.INSERT_Table_D,
            'W':self.INSERT_Table_W,
            'M':self.INSERT_Table_M,
            '5':self.INSERT_Table_5,
            '15':self.INSERT_Table_15,
            '30':self.INSERT_Table_30,  
            '60':self.INSERT_Table_60,
            }
         return switcher[ktype](code,start,end,ktype)    

    def INSERT_Table_D(sel,code,start,end,ktype):  
       df = ts.get_hist_data(code,start,end,ktype)
       engine =create_engine("mysql+pymysql://root:123456789@localhost:3306/testsql",encoding="utf-8",echo=True) 
       #存入数据库
       try:
          df.to_sql('Historical_Data_'+code+'_D',engine,if_exists='append')
       except:
          pass
       finally:
          pass
    def INSERT_Table_W(sel,code,start,end,ktype):  
       df = ts.get_hist_data(code,start,end,ktype)
       engine =create_engine("mysql+pymysql://root:123456789@localhost:3306/testsql",encoding="utf-8",echo=True) 
       #存入数据库
       try:
          df.to_sql('Historical_Data_'+code+'_W',engine,if_exists='append')
       except:
          pass
       finally:
          pass
    def INSERT_Table_M(sel,code,start,end,ktype):  
       df = ts.get_hist_data(code,start,end,ktype)
       engine =create_engine("mysql+pymysql://root:123456789@localhost:3306/testsql",encoding="utf-8",echo=True) 
       #存入数据库
       try:
          df.to_sql('Historical_Data_'+code+'_D',engine,if_exists='append')
       except:
          pass
       finally:
          pass
    def INSERT_Table_5(sel,code,start,end,ktype):  
       df = ts.get_hist_data(code,start,end,ktype)
       engine =create_engine("mysql+pymysql://root:123456789@localhost:3306/testsql",encoding="utf-8",echo=True) 
       #存入数据库
       try:
          df.to_sql('Historical_Data_'+code+'_5m',engine,if_exists='append')
       except:
          pass
       finally:
          pass
    def INSERT_Table_15(sel,code,start,end,ktype):  
       df = ts.get_hist_data(code,start,end,ktype)
       engine =create_engine("mysql+pymysql://root:123456789@localhost:3306/testsql",encoding="utf-8",echo=True) 
       #存入数据库
       try:
          df.to_sql('Historical_Data_'+code+'_15m',engine,if_exists='append')
       except:
          pass
       finally:
          pass
    def INSERT_Table_30(sel,code,start,end,ktype):  
       df = ts.get_hist_data(code,start,end,ktype)
       engine =create_engine("mysql+pymysql://root:123456789@localhost:3306/testsql",encoding="utf-8",echo=True) 
       #存入数据库
       try:
          df.to_sql('Historical_Data_'+code+'_30m',engine,if_exists='append')
       except:
          pass
       finally:
          pass
    def INSERT_Table_60(sel,code,start,end,ktype):  
       df = ts.get_hist_data(code,start,end,ktype)
       engine =create_engine("mysql+pymysql://root:123456789@localhost:3306/testsql",encoding="utf-8",echo=True) 
       #存入数据库
       try:
          df.to_sql('Historical_Data_'+code+'_60m',engine,if_exists='append')
       except:
          pass
       finally:
          pass
