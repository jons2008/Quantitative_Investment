import tushare as ts
from sqlalchemy import create_engine

class CreateHistoricalData():

    def __init__(self,parent=None):
        pass

    #def Update_Stock_Data(self,code,start,end,ktype,retry_count=3,pause=0):
    #    #df=ts.get_profit_data(2014,3)
    #    #pass
    #    #for stock in df:
    #    self.CREATE_TABLE(ktype,code)
    #    self.INSERT_TABLE(code,start,end,ktype)
    #   #df = ts.get_hist_data(code,start,end,ktype)
    #   #engine =create_engine("mysql+pymysql://root:123456789@localhost:3306/testsql",encoding="utf-8",echo=True) 
    #   ##存入数据库
    #   #try:
    #   #   df.to_sql('tick_data',engine)
    #   #except:
    #   #    try:
    #   #        df.to_sql('tick_data',engine,if_exists='replace')
    #   #    except:
    #   #        df.to_sql('tick_data',engine,if_exists='append')
    #   #        pass
    #   #    finally:
    #   #        pass
    #   #finally:
    #   #    pass
    #
    #
    def CREATE_TABLE(self,ktype,code):
         switcher = {
            'D':self.Create_Table_D,
            'W':self.Create_Table_W,
            'M':self.Create_Table_M,
            '5':self.Create_Table_5,
            '15':self.Create_Table_15,
            '30':self.Create_Table_30,  
            '60':self.Create_Table_60,
            }
         return switcher[ktype](code)
    
    def Create_Table_D(self,code):  
       #df = ts.get_hist_data(code)
       engine =create_engine("mysql+pymysql://root:123456789@localhost:3306/testsql",encoding="utf-8",echo=True) 
       #存入数据库
       try:
          df.to_sql('Historical_Data_'+code+'_D',engine)
       except:
           pass
       finally:
           pass

    
    def Create_Table_W(self):  
       #df = ts.get_hist_data(code)
       engine =create_engine("mysql+pymysql://root:123456789@localhost:3306/testsql",encoding="utf-8",echo=True) 
       #存入数据库
       try:
          df.to_sql('Historical_Data_'+code+'_W',engine)
       except:
           pass
       finally:
           pass
    def Create_Table_M(self): 
       #df = ts.get_hist_data(code)
       engine =create_engine("mysql+pymysql://root:123456789@localhost:3306/testsql",encoding="utf-8",echo=True) 
       #存入数据库
       try:
          df.to_sql('Historical_Data_'+code+'_M',engine)
       except:
           pass
       finally:
           pass
    def Create_Table_5(self): 
       #df = ts.get_hist_data(code)
       engine =create_engine("mysql+pymysql://root:123456789@localhost:3306/testsql",encoding="utf-8",echo=True) 
       #存入数据库
       try:
          df.to_sql('Historical_Data_'+code+'_5m',engine)
       except:
           pass
       finally:
           pass
    def Create_Table_15(self):  
       #df = ts.get_hist_data(code)
       engine =create_engine("mysql+pymysql://root:123456789@localhost:3306/testsql",encoding="utf-8",echo=True) 
       #存入数据库
       try:
          df.to_sql('Historical_Data_'+code+'_15m',engine)
       except:
           pass
       finally:
           pass
    def Create_Table_30(self):  
       #df = ts.get_hist_data(code)
       engine =create_engine("mysql+pymysql://root:123456789@localhost:3306/testsql",encoding="utf-8",echo=True) 
       #存入数据库
       try:
          df.to_sql('Historical_Data_'+code+'_30m',engine)
       except:
           pass
       finally:
           pass
    def Create_Table_60(self): 
       #df = ts.get_hist_data(code)
       engine =create_engine("mysql+pymysql://root:123456789@localhost:3306/testsql",encoding="utf-8",echo=True) 
       #存入数据库
       try:
          df.to_sql('Historical_Data_'+code+'_60m',engine)
       except:
           pass
       finally:
           pass