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

    def Delete_Table(self,ktype,code,start,end):  
        try:
            mycursor = mydb.cursor()
            sql = "DELETE FROM Historical_Data_"+code+" WHERE DATE>='"+start+"' AND DATE<='"+end+"' AND Ktype='"+ktype+"'"
            mycursor.execute(sql)
            mydb.commit()
        except:
            mydb.rollback()
        finally:
            #mydb.close()
            pass
 