import tushare as ts
from sqlalchemy import create_engine
import time
import pymysql
HOSTNAME = "localhost"
PORT = "3306"
DATABASE = "stock_historical_data"
USERNAME = "root"
PASSWORD = "123456789"
mydb = pymysql.connect(
  HOSTNAME,
  USERNAME,
  PASSWORD,
  DATABASE
)
class CreateHistoricalData():
    
    def __init__(self,parent=None):
        pass
    def Create_Table_Historical_Data(self,ktype,code):  
        try:
            mycursor = mydb.cursor()
            sql='CREATE TABLE IF NOT EXISTS `Historical_Data_'+code+'`('
            sql=sql+'`date` VARCHAR(100),'
            sql=sql+'`open` double(16,2),'
            sql=sql+'`high` double(16,2),'
            sql=sql+'`close` double(16,2),'
            sql=sql+'`volume` double(16,2),'
            sql=sql+'`low` double(16,2),'
            sql=sql+'`price_change` double(16,2),'
            sql=sql+'`p_change` double(16,2),'
            sql=sql+'`ma5` double(16,2),'
            sql=sql+'`ma10` double(16,2),'
            sql=sql+'`ma20` double(16,2),'
            sql=sql+'`v_ma5` double(16,2),'
            sql=sql+'`v_ma10`double(16,2),'
            sql=sql+'`v_ma20` double(16,2),'
            sql=sql+'`ktype` VARCHAR(100)'
            sql=sql+')ENGINE=InnoDB DEFAULT CHARSET=utf8;'
            #df.to_sql('Historical_Data_'+code,engine)
            mycursor.execute(sql)
            mydb.commit()
        except:
           pass
        finally:
           #mydb.close()
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