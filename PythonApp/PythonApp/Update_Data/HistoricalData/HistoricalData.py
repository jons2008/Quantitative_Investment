import tushare as ts
from sqlalchemy import create_engine
import time
import pymysql
import sqlalchemy
from sqlalchemy import create_engine 
import pandas as pd
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
class HistoricalData():
    def __init__(self,parent=None):
        pass
    def Create(self,ktype,code):  
        try:
            mydb = pymysql.connect(HOSTNAME,USERNAME,PASSWORD,DATABASE)
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
           mydb.close()
           pass

    def Delete(self,ktype,code,start,end):  
        try:
            mydb = pymysql.connect(HOSTNAME,USERNAME,PASSWORD,DATABASE)
            mycursor = mydb.cursor()
            sql = "DELETE FROM Historical_Data_"+code+" WHERE DATE>='"+str(start)+"' AND DATE<='"+str(end)+"' AND Ktype='"+ktype+"'"
            mycursor.execute(sql)
            mydb.commit()
        except:
            mydb.rollback()
        finally:
            mydb.close()
            pass
    def Select(self,code,start,end,ktype):
        result=""
        try:
            mydb = pymysql.connect(HOSTNAME,USERNAME,PASSWORD,DATABASE)
            mycursor = mydb.cursor()
            sql = "SELECT * FROM Historical_Data_"+code+" WHERE DATE>='"+str(start)+"' AND DATE<='"+str(end)+"' AND Ktype='"+ktype+"'"
            mycursor.execute(sql)
            result=mycursor.fetchall() 
        except:
            mydb.rollback()
        finally:
            mydb.close()
            return result
            pass
        
        
    def INSERT(self,code,start,end,ktype):  
       Is_While=True
       
       while (Is_While):
           try:
                mydb = pymysql.connect(HOSTNAME,USERNAME,PASSWORD,DATABASE)
                df = ts.get_hist_data(code,start,end,ktype)
                if df is not None:
                    if len(df)!=0:
                        df["ktype"]=ktype

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
                        Is_While=False
                    else:
                        Is_While=False
                else:
                    Is_While=False
           except:
               Is_While=True
               mydb.rollback()
           finally:
               mydb.close()
               pass