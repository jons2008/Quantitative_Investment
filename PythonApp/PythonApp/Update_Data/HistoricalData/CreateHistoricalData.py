import tushare as ts
from sqlalchemy import create_engine
import time
class CreateHistoricalData():

    def __init__(self,parent=None):
        pass

    def CREATE_TABLE(self,ktype,code):
         #switcher = {
         #   'D':self.Create_Table_Historical_Data_
         #   #'W':self.Create_Table_W,
         #   #'M':self.Create_Table_M,
         #   #'5':self.Create_Table_5,
         #   #'15':self.Create_Table_15,
         #   #'30':self.Create_Table_30,  
         #   #'60':self.Create_Table_60,
         #   }
         #return switcher[ktype](code,ktype)
         pass
    
    def Create_Table_Historical_Data(self,ktype,code,retry_count,pause):  
       df = ts.get_hist_data(code,retry_count=retry_count,pause=pause)
       df["ktype"]=ktype
       engine =create_engine("mysql+pymysql://root:123456789@localhost:3306/testsql",encoding="utf-8",echo=True) 
       #存入数据库
       try:
          df.to_sql('Historical_Data_'+code,engine)
       except:
           pass
       finally:
           pass

    
    def CREATE_TICK_DATA(self,code):  
       df = ts.get_today_ticks(code)
       df['data']=time.strftime("%Y-%m-%d", time.localtime()) 
       engine =create_engine("mysql+pymysql://root:123456789@localhost:3306/testsql",encoding="utf-8",echo=True) 
       #存入数据库
       try:
          df.to_sql('today_ticks_'+code,engine)
       except:
           pass
       finally:
           pass
    #def Create_Table_M(self): 
    #   df = ts.get_hist_data(code)
    #   engine =create_engine("mysql+pymysql://root:123456789@localhost:3306/testsql",encoding="utf-8",echo=True) 
    #   #存入数据库
    #   try:
    #      df.to_sql('Historical_Data_'+code+'_M',engine)
    #   except:
    #       pass
    #   finally:
    #       pass
    #def Create_Table_5(self): 
    #   df = ts.get_hist_data(code)
    #   engine =create_engine("mysql+pymysql://root:123456789@localhost:3306/testsql",encoding="utf-8",echo=True) 
    #   #存入数据库
    #   try:
    #      df.to_sql('Historical_Data_'+code+'_5m',engine)
    #   except:
    #       pass
    #   finally:
    #       pass
    #def Create_Table_15(self):  
    #   df = ts.get_hist_data(code)
    #   engine =create_engine("mysql+pymysql://root:123456789@localhost:3306/testsql",encoding="utf-8",echo=True) 
    #   #存入数据库
    #   try:
    #      df.to_sql('Historical_Data_'+code+'_15m',engine)
    #   except:
    #       pass
    #   finally:
    #       pass
    #def Create_Table_30(self):  
    #   df = ts.get_hist_data(code)
    #   engine =create_engine("mysql+pymysql://root:123456789@localhost:3306/testsql",encoding="utf-8",echo=True) 
    #   #存入数据库
    #   try:
    #      df.to_sql('Historical_Data_'+code+'_30m',engine)
    #   except:
    #       pass
    #   finally:
    #       pass
    #def Create_Table_60(self): 
    #   df = ts.get_hist_data(code)
    #   engine =create_engine("mysql+pymysql://root:123456789@localhost:3306/testsql",encoding="utf-8",echo=True) 
    #   #存入数据库
    #   try:
    #      df.to_sql('Historical_Data_'+code+'_60m',engine)
    #   except:
    #       pass
    #   finally:
    #       pass