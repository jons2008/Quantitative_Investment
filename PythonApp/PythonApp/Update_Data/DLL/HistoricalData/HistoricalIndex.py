
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
class HistoricalIndex():
    def __init__(self,parent=None):
        pass
    def Create(self):  
        try:
            mydb = pymysql.connect(HOSTNAME,USERNAME,PASSWORD,DATABASE)
            mycursor = mydb.cursor()
            sql='CREATE TABLE IF NOT EXISTS `HistoricalIndex`('
            sql=sql+'`code` VARCHAR(100),'
            sql=sql+'`name` VARCHAR(100),'
            sql=sql+'`change` VARCHAR(100),'
            sql=sql+'`open` double(16,2),'
            sql=sql+'`preclose` double(16,2),'
            sql=sql+'`close` double(16,2),'
            sql=sql+'`high` double(16,2),'
            sql=sql+'`low` double(16,2),'
            sql=sql+'`volume` double(16,2),'
            sql=sql+'`amount` double(16,2)'
            sql=sql+'`Datetime` VARCHAR(100)'
            sql=sql+')ENGINE=InnoDB DEFAULT CHARSET=utf8;'
            #df.to_sql('Historical_Data_'+code,engine)
            mycursor.execute(sql)
            mydb.commit()
        except:
           pass
        finally:
           mydb.close()
           pass

    def Delete(self,Datetime):  
        try:
            mydb = pymysql.connect(HOSTNAME,USERNAME,PASSWORD,DATABASE)
            mycursor = mydb.cursor()
            sql = "DELETE FROM HistoricalIndex WHERE Datetime='"+str(Datetime)+"'"
            mycursor.execute(sql)
            mydb.commit()
        except:
            mydb.rollback()
        finally:
            mydb.close()
            pass
    def Select(self,Datetime):
        result=""
        try:
            mydb = pymysql.connect(HOSTNAME,USERNAME,PASSWORD,DATABASE)
            mycursor = mydb.cursor()
            sql = "SELECT * FROM HistoricalIndex WHERE Datetime='"+str(Datetime)+"'"
            mycursor.execute(sql)
            result=mycursor.fetchall() 
        except:
            mydb.rollback()
        finally:
            mydb.close()
            return result
            pass
        
        
    def INSERT(self):  
       Is_While=True
       mydb = pymysql.connect(HOSTNAME,USERNAME,PASSWORD,DATABASE)
       while (Is_While):
           try:
                df = ts.get_index()
                if len(df)!=0:
                    df["Datetime"]=time.strftime("%Y-%m-%d", time.localtime())
                    mycursor = mydb.cursor()
                    for index, row in df.iterrows():
                        sql = 'INSERT INTO HistoricalIndex (code,name,change,open,preclose,close,high,low,volume,amount,Datetime)'
                        sql = sql+'VALUES("'+str(row["code"])+'"'
                        sql = sql+','+str(row["name"])
                        sql = sql+','+str(row["change"])
                        sql = sql+','+str(row["open"])
                        sql = sql+','+str(row["preclose"])
                        sql = sql+','+str(row["close"])
                        sql = sql+','+str(row["high"])
                        sql = sql+','+str(row["low"])
                        sql = sql+','+str(row["volume"])
                        sql = sql+','+str(row["Datetime"])
                        sql = sql+')'
                        mycursor.execute(sql)
                    mydb.commit()
                    Is_While=False
           except:
               Is_While=True
               mydb.rollback()
           finally:
               mydb.close()
               pass