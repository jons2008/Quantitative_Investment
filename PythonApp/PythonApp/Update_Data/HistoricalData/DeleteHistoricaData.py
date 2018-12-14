from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
import unittest
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
class DeleteHistoricaData():

    def __init__(self,parent=None):
        pass
    def Delete_TABLE(self,ktype,code,start,end):
    #     switcher = {
    #        'D':self.Delete_Table_D,
    #        'W':self.Delete_Table_W,
    #        'M':self.Delete_Table_M,
    #        '5':self.Delete_Table_5,
    #        '15':self.Delete_Table_15,
    #        '30':self.Delete_Table_30,  
    #        '60':self.Delete_Table_60,
    #        }
    #     return switcher[ktype](code,start,end)
    #
        pass
    def Delete_Table(self,ktype,code,start,end):  
        try:
            mycursor = mydb.cursor()
            sql = "DELETE FROM Historical_Data_"+code+"_"+ktype+" WHERE DATE>='"+start+"' AND DATE<='"+end+"' AND Ktype='"+ktype+"'"
            mycursor.execute(sql)
            mydb.commit()
        except:
            mydb.rollback()
        finally:
            #mydb.close()
            pass
    #def Delete_Table_W(sel,code,start,end):  
    #   try:
    #        mycursor = mydb.cursor()
    #        sql = "DELETE FROM Historical_Data_"+code+"_W WHERE DATE>='"+start+"' AND DATE<='"+end+"'"
    #        mycursor.execute(sql)
    #        mydb.commit()
    #   except:
    #        mydb.rollback()
    #   finally:
    #        mydb.close()
    #def Delete_Table_M(sel,code,start,end):  
    #   try:
    #        mycursor = mydb.cursor()
    #        sql = "DELETE FROM Historical_Data_"+code+"_M WHERE DATE>='"+start+"' AND DATE<='"+end+"'"
    #        mycursor.execute(sql)
    #        mydb.commit()
    #   except:
    #        mydb.rollback()
    #   finally:
    #        mydb.close()
    #def Delete_Table_5(sel,code,start,end):  
    #   try:
    #        mycursor = mydb.cursor()
    #        sql = "DELETE FROM Historical_Data_"+code+"_5m WHERE DATE>='"+start+"' AND DATE<='"+end+"'"
    #        mycursor.execute(sql)
    #        mydb.commit()
    #   except:
    #        mydb.rollback()
    #   finally:
    #        mydb.close()
    #def Delete_Table_15(sel,code,start,end):  
    #   try:
    #        mycursor = mydb.cursor()
    #        sql = "DELETE FROM Historical_Data_"+code+"_15m WHERE DATE>='"+start+"' AND DATE<='"+end+"'"
    #        mycursor.execute(sql)
    #        mydb.commit()
    #   except:
    #        mydb.rollback()
    #   finally:
    #        mydb.close()
    #def Delete_Table_30(sel,code,start,end):  
    #   try:
    #        mycursor = mydb.cursor()
    #        sql = "DELETE FROM Historical_Data_"+code+"_30m WHERE DATE>='"+start+"' AND DATE<='"+end+"'"
    #        mycursor.execute(sql)
    #        mydb.commit()
    #   except:
    #        mydb.rollback()
    #   finally:
    #        mydb.close()
    #def Delete_Table_60(sel,code,start,end):  
    #   try:
    #        mycursor = mydb.cursor()
    #        sql = "DELETE FROM Historical_Data_"+code+"_60m WHERE DATE>='"+start+"' AND DATE<='"+end+"'"
    #        mycursor.execute(sql)
    #        mydb.commit()
    #   except:
    #        mydb.rollback()
    #   finally:
    #        mydb.close()