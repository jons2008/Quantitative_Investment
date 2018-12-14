import tushare as ts
from Update_Data.HistoricalData import DeleteHistoricaData
from Update_Data.HistoricalData.CreateHistoricalData import CreateHistoricalData
from sqlalchemy import create_engine 
import pymysql
import time
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
class InsertHistoricalData():
    def __init__(self,parent=None):
        pass
    def Insert_Historical_Data(self,code,start,end,ktype):
        
        CreateTable=CreateHistoricalData()
        
        CreateTable.Create_Table_Historical_Data(ktype=ktype,code=code)
        DelTable=DeleteHistoricaData.DeleteHistoricaData()
        DelTable.Delete_Table(ktype=ktype,code=code,start=start,end=end)
        self.INSERT_TABLE(code,start,end,ktype)

    def SET_Insert_TICK_DATA(self,code):
        self.INSERT_TODAY_TICKS(code)

    def INSERT_TABLE(self,code,start,end,ktype):  
       df = ts.get_hist_data(code,start,end,ktype)
       df["ktype"]=ktype
       try:
            mycursor = mydb.cursor()
            for index, row in df.iterrows():
                sql = 'INSERT INTO historical_data_'+code+' (date,open,high,close,low,volume,price_change,p_change,ma5,ma10,ma20,v_ma5,v_ma10,v_ma20,ktype)'
                sql = sql+'VALUES("'+index+'"'
                sql = sql+','+str(row["open"])
                sql = sql+','+str(row["high"])
                sql = sql+','+str(row["close"])
                sql = sql+','+str(row["low"])
                sql = sql+','+str(row["volume"])
                sql = sql+','+str(row["price_change"])
                sql = sql+','+str(row["p_change"])
                sql = sql+','+str(row["ma5"])
                sql = sql+','+str(row["ma10"])
                sql = sql+','+str(row["ma20"])
                sql = sql+','+str(row["v_ma5"])
                sql = sql+','+str(row["v_ma10"])
                sql = sql+','+str(row["v_ma20"])
                sql = sql+',"'+str(row["ktype"])+'")'
                mycursor.execute(sql)
                mydb.commit()
       except:
            mydb.rollback()
       finally:
            #mydb.close()
            pass
    def INSERT_TODAY_TICKS(self,code):  
       try:
           df = ts.get_today_ticks(code)
           df['data']=time.strftime("%Y-%m-%d", time.localtime()) 
           mycursor = mydb.cursor()
           for index, row in df.iterrows():
               sql = 'INSERT INTO today_ticks_'+code+' (time,price,pchange,change,volume,amount,type,data)'
               sql = sql+'VALUES("'+index+'"'
               sql = sql+','+str(row["time"])
               sql = sql+','+str(row["price"])
               sql = sql+','+str(row["pchange"])
               sql = sql+','+str(row["change"])
               sql = sql+','+str(row["volume"])
               sql = sql+','+str(row["amount"])
               sql = sql+','+str(row["type"])
               sql = sql+','+str(row["data"])
               sql = sql+'")'
               mycursor.execute(sql)
               mydb.commit()
       except:
            mydb.rollback()
       finally:
            #mydb.close()
            pass
    #def INSERT_Table_M(sel,code,start,end,ktype):  
    #   df = ts.get_hist_data(code,start,end,ktype)
    #   engine =create_engine("mysql+pymysql://root:123456789@localhost:3306/testsql",encoding="utf-8",echo=True) 
    #   #存入数据库
    #   try:
    #      df.to_sql('Historical_Data_'+code+'_D',engine,if_exists='append')
    #   except:
    #      pass
    #   finally:
    #      pass
    #def INSERT_Table_5(sel,code,start,end,ktype):  
    #   df = ts.get_hist_data(code,start,end,ktype)
    #   engine =create_engine("mysql+pymysql://root:123456789@localhost:3306/testsql",encoding="utf-8",echo=True) 
    #   #存入数据库
    #   try:
    #      df.to_sql('Historical_Data_'+code+'_5m',engine,if_exists='append')
    #   except:
    #      pass
    #   finally:
    #      pass
    #def INSERT_Table_15(sel,code,start,end,ktype):  
    #   df = ts.get_hist_data(code,start,end,ktype)
    #   engine =create_engine("mysql+pymysql://root:123456789@localhost:3306/testsql",encoding="utf-8",echo=True) 
    #   #存入数据库
    #   try:
    #      df.to_sql('Historical_Data_'+code+'_15m',engine,if_exists='append')
    #   except:
    #      pass
    #   finally:
    #      pass
    #def INSERT_Table_30(sel,code,start,end,ktype):  
    #   df = ts.get_hist_data(code,start,end,ktype)
    #   engine =create_engine("mysql+pymysql://root:123456789@localhost:3306/testsql",encoding="utf-8",echo=True) 
    #   #存入数据库
    #   try:
    #      df.to_sql('Historical_Data_'+code+'_30m',engine,if_exists='append')
    #   except:
    #      pass
    #   finally:
    #      pass
    #def INSERT_Table_60(sel,code,start,end,ktype):  
    #   df = ts.get_hist_data(code,start,end,ktype)
    #   engine =create_engine("mysql+pymysql://root:123456789@localhost:3306/testsql",encoding="utf-8",echo=True) 
    #   #存入数据库
    #   try:
    #      df.to_sql('Historical_Data_'+code+'_60m',engine,if_exists='append')
    #   except:
    #      pass
    #   finally:
    #      pass
    #