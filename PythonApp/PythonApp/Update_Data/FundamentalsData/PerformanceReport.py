import tushare as ts
from sqlalchemy import create_engine
import time
import pymysql
import sqlalchemy
from sqlalchemy import create_engine 
import pandas as pd
HOSTNAME = "localhost"
PORT = "3306"
DATABASE = "stock_fundamentals"
USERNAME = "root"
PASSWORD = "123456789"

#业绩报告
#按年度、季度获取业绩报表数据。数据获取需要一定的时间，网速取决于您的网速，请耐心等待。结果返回的数据属性说明如下：
class PerformanceReport():
    def __init__(self,parent=None):
        pass
    def Create(self):  
        try:
            mydb = pymysql.connect(HOSTNAME,USERNAME,PASSWORD,DATABASE)
            mycursor = mydb.cursor()
            sql='CREATE TABLE IF NOT EXISTS PerformanceReport('
            sql=sql+'`Year` VARCHAR(100),'#年
            sql=sql+'`Month` VARCHAR(100),'#月
            sql=sql+'`code` VARCHAR(100),'#代码
            sql=sql+'`name` VARCHAR(100),'#名称
            sql=sql+'`eps` VARCHAR(100),'#每股收益
            sql=sql+'`eps_yoy` VARCHAR(100),'#每股收益同比(%)
            sql=sql+'`bvps` VARCHAR(100),'#每股净资产
            sql=sql+'`roe` VARCHAR(100),'#净资产收益率(%)
            sql=sql+'`epcf` VARCHAR(100),'#每股现金流量(元)
            sql=sql+'`net_profits` VARCHAR(100),'#净利润(万元)
            sql=sql+'`profits_yoy` VARCHAR(100),'#净利润同比(%)
            sql=sql+'`distrib` VARCHAR(100),'#,分配方案
            sql=sql+'`report_date` VARCHAR(100)'#发布日期
            sql=sql+')ENGINE=InnoDB DEFAULT CHARSET=utf8;'
            #df.to_sql('Historical_Data_'+code,engine)
            mycursor.execute(sql)
            mydb.commit()
        except:
           pass
        finally:
           mydb.close()
           pass

    def Delete(self,Year,Month):  
        try:
            mydb = pymysql.connect(HOSTNAME,USERNAME,PASSWORD,DATABASE)
            mycursor = mydb.cursor()
            sql = "DELETE FROM PerformanceReport WHERE Year='"+str(Year)+"' AND Month='"+str(Month)+"'"
            mycursor.execute(sql)
            mydb.commit()
        except:
            mydb.rollback()
        finally:
            mydb.close()
            pass

    def Select(self,Year,Month):  
        result=""
        try:
            mydb = pymysql.connect(HOSTNAME,USERNAME,PASSWORD,DATABASE)
            mycursor = mydb.cursor()
            sql = "SELECT * FROM PerformanceReport WHERE Year='"+str(Year)+"' AND Month='"+str(Month)+"'"
            mycursor.execute(sql)
            result=mycursor.fetchall() 
        except:
            mydb.rollback()
        finally:
            mydb.close()
            return result
            pass
        
        
    def INSERT(self,Year,Month):  
       Is_While=True
       mydb = pymysql.connect(HOSTNAME,USERNAME,PASSWORD,DATABASE)
       while (Is_While):
           try:
                df = ts.get_report_data(Year,Month)
                df=df.where(df.notnull(),'NaN')
                
                if len(df)!=0:
                    mycursor = mydb.cursor()
                    for index, row in df.iterrows():
                        sql = 'INSERT INTO PerformanceReport (code,name,eps,eps_yoy,bvps,roe,epcf,net_profits,profits_yoy,distrib,report_date,Year,Month)'
                        sql = sql+'VALUES("'+str(row["code"])+'"'
                        sql = sql+',"'+str(row["name"])+'"'
                        sql = sql+',"'+str(row["eps"])+'"'
                        sql = sql+',"'+str(row["eps_yoy"])+'"'
                        sql = sql+',"'+str(row["bvps"])+'"'
                        sql = sql+',"'+str(row["roe"])+'"'
                        sql = sql+',"'+str(row["epcf"])+'"'
                        sql = sql+',"'+str(row["net_profits"])+'"'
                        sql = sql+',"'+str(row["profits_yoy"])+'"'
                        sql = sql+',"'+str(row["distrib"])+'"'
                        sql = sql+',"'+str(row["report_date"])+'"'
                        sql = sql+',"'+str(Year)+'"'
                        sql = sql+',"'+str(Month)+'"'
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
