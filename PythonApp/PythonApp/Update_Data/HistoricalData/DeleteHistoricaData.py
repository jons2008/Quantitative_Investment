from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
import unittest
import mysql.connector
HOSTNAME = "localhost"
PORT = "3306"
DATABASE = "testsql"
USERNAME = "root"
PASSWORD = "123456789"
mydb = mysql.connector.connect(
  host=HOSTNAME,
  user=USERNAME,
  passwd=PASSWORD,
  database=DATABASE
)
class DeleteHistoricaData():

    def __init__(self,parent=None):
        pass
    def Delete_TABLE(self,ktype,code,start,end):
         switcher = {
            'D':self.Delete_Table_D,
            'W':self.Delete_Table_W,
            'M':self.Delete_Table_M,
            '5':self.Delete_Table_5,
            '15':self.Delete_Table_15,
            '30':self.Delete_Table_30,  
            '60':self.Delete_Table_60,
            }
         return switcher[ktype](code,start,end)

    def Delete_Table_D(sel,code,start,end):  
        try:
            mycursor = mydb.cursor()
            sql = "DELETE FROM Historical_Data_"+code+"_d WHERE DATE>='"+start+"' AND DATE<='"+end+"'"
            mycursor.execute(sql)
            mydb.commit()
        except:
           pass
        finally:
           pass
    def Delete_Table_W(sel,code,start,end):  
       try:
            r1 = connect.execute("SELECT * FROM `Historical_Data_"+code+"_W` WHERE DATE>='2017-03-20' AND DATE<='2017-04-20' ") #执行查询
            for u in r1:
                x=session.query(User).filter(User.date==str(u['date'])).delete()
            session.commit()
           
       except:
          pass
       finally:
          pass
    def Delete_Table_M(sel,code,start,end):  
       try:
           r1 = connect.execute("SELECT * FROM `Historical_Data_"+code+"_M` WHERE DATE>='2017-03-20' AND DATE<='2017-04-20' ") #执行查询
           for u in r1:
               x=session.query(User).filter(User.date==str(u['date'])).delete()
           session.commit()
       except:
          pass
       finally:
          pass
    def Delete_Table_5(sel,code,start,end):  
       try:
           r1 = connect.execute("SELECT * FROM `Historical_Data_"+code+"_5m` WHERE DATE>='2017-03-20' AND DATE<='2017-04-20' ") #执行查询
           for u in r1:
               x=session.query(User).filter(User.date==str(u['date'])).delete()
           session.commit()
       except:
          pass
       finally:
          pass
    def Delete_Table_15(sel,code,start,end):  
       try:
           # 执行SQL
           r1 = connect.execute("SELECT * FROM `Historical_Data_"+code+"_15m` WHERE DATE>='2017-03-20' AND DATE<='2017-04-20' ") #执行查询
           for u in r1:
               x=session.query(User).filter(User.date==str(u['date'])).delete()
           session.commit()
       except:
          pass
       finally:
          pass
    def Delete_Table_30(sel,code,start,end):  
       
       try:
           r1 = connect.execute("SELECT * FROM `Historical_Data_"+code+"_30m` WHERE DATE>='2017-03-20' AND DATE<='2017-04-20' ") #执行查询
           for u in r1:
               x=session.query(User).filter(User.date==str(u['date'])).delete()
           session.commit()
       except:
          pass
       finally:
          pass

    def Delete_Table_60(sel,code,start,end):  
       #存入数据库
       try:
           r1 = connect.execute("SELECT * FROM `Historical_Data_"+code+"_60m` WHERE DATE>='2017-03-20' AND DATE<='2017-04-20' ") #执行查询
           for u in r1:
               x=session.query(User).filter(User.date==str(u['date'])).delete()
           session.commit()
       except:
          pass
       finally:
          pass