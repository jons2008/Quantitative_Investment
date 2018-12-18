import tushare as ts
import sqlalchemy
from sqlalchemy import create_engine 
import time
import pymysql

HOSTNAME = "localhost"
PORT = "3306"
DATABASE = "stock_today_ticks"
USERNAME = "root"
PASSWORD = "123456789"

connect_info = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)  #1
engine = create_engine(connect_info)
HOSTNAME = "localhost"
PORT = "3306"
DATABASE = "stock_today_ticks"
USERNAME = "root"
PASSWORD = "123456789"

connect_info = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)  #1
engine = create_engine(connect_info)
class TodayTicks():
    def __init__(self,parent=None):
        pass
    def Create(self,code):  
        try:
            mydb = pymysql.connect(HOSTNAME,USERNAME,PASSWORD,DATABASE)
            mycursor = mydb.cursor()
            sql='CREATE TABLE IF NOT EXISTS `Today_Ticks_'+code+'`('
            sql=sql+'`date` VARCHAR(100),'
            sql=sql+'`time` VARCHAR(100),'
            sql=sql+'`price` VARCHAR(100),'
            sql=sql+'`pchange` VARCHAR(100),'
            sql=sql+'`change` VARCHAR(100),'
            sql=sql+'`volume` VARCHAR(100),'
            sql=sql+'`amount` VARCHAR(100),'
            sql=sql+'`type` VARCHAR(100)'
            sql=sql+')ENGINE=InnoDB DEFAULT CHARSET=utf8;'
            #df.to_sql('Historical_Data_'+code,engine)
            mycursor.execute(sql)
            mydb.commit()
        except:
           mydb.rollback()
           pass
        finally:
           mydb.close()
           pass

    def Delete(self,code,date):  
        try:
            mydb = pymysql.connect(HOSTNAME,USERNAME,PASSWORD,DATABASE)
            mycursor = mydb.cursor()
            sql = "DELETE FROM TODAY_TICKS_"+code+" WHERE DATE='"+str(date)+"'"
            mycursor.execute(sql)
            mydb.commit()
        except:
            mydb.rollback()
        finally:
            mydb.close()
            pass
    def INSERT(self,code):  
       Is_While=True
       while (Is_While):
           try:
               mydb = pymysql.connect(HOSTNAME,USERNAME,PASSWORD,DATABASE)
               #time.sleep(1)
               df = ts.get_today_ticks(code,retry_count=20)
               if len(df)!=0:
                   df['data']=time.strftime("%Y-%m-%d", time.localtime()) 
                   mycursor = mydb.cursor()
                   for index, row in df.iterrows():
                        sql = "INSERT INTO `stock_today_ticks`.`TODAY_TICKS_"+code+"` (`date`,`time`,`price`,`pchange`,`change`,`volume`,`amount`,`type`)"
                        sql = sql+"VALUES('"+str(row["data"])+"'"
                        sql = sql+",'"+str(row["time"])+"'"
                        sql = sql+",'"+str(row["price"])+"'"
                        sql = sql+",'"+str(row["pchange"])+"'"
                        sql = sql+",'"+str(row["change"])+"'"
                        sql = sql+",'"+str(row["volume"])+"'"
                        sql = sql+",'"+str(row["amount"])+"'"
                        sql = sql+",'"+str(row["type"])+"'"
                        sql = sql+")"
                        mycursor.execute(sql)
                   mydb.commit()
                   Is_While=False
               else:
                   Is_While=True
           except:
               Is_While=True
               mydb.rollback()
               pass
           finally:
               mydb.close()
               pass
    def Select(self,code,date):
        result=""
        try:
            mydb = pymysql.connect(HOSTNAME,USERNAME,PASSWORD,DATABASE)
            mycursor = mydb.cursor()
            sql = "SELECT * FROM TODAY_TICKS_"+code+" WHERE DATE='"+str(date)+"'"
            mycursor.execute(sql)
            result=mycursor.fetchall() 
        except:
            mydb.rollback()
        finally:
            mydb.close()
            return result
            pass
