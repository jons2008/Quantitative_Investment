import tushare as ts
from sqlalchemy import create_engine
class InsertHistoricalData():

    def __init__(self,parent=None):
        pass

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
          df.to_sql('Historical_Data_'+code+'_M',engine,if_exists='append')
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