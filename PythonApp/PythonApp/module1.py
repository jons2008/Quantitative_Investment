import tushare as ts
import sqlalchemy
from sqlalchemy import create_engine 
import time
import pymysql
import threading
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
               df = ts.get_today_ticks(code,retry_count=5)
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

class Thread_Bll_HisData(threading.Thread):
    def __init__(self,df):
        threading.Thread.__init__(self)
        self.df = df
    def run(self):
       #print "Starting " + self.name
       # 获得锁，成功获得锁定后返回True
       # 可选的timeout参数不填时将一直阻塞直到获得锁定
       # 否则超时后将返回False
        #threadLock.acquire()
       for code in self.df:
           #print(code)
           CreateTable=TodayTicks()
           if len(CreateTable.Select(code,time.strftime("%Y-%m-%d", time.localtime())))==0:
               CreateTable.Create(code)
               CreateTable.Delete(code,date=time.strftime("%Y-%m-%d", time.localtime()))
               CreateTable.INSERT(code)
        #bll_hisdata=Bll_HisData()
        #bll_hisdata.Insert_Historical_Data(self.code1,self.start1,self.end1,self.ktype1)
        # 释放锁
        #threadLock.release() 
df = ts.get_stock_basics()
threads = []
i=0
count=int(len(df)/5)
#print(df.index[0:count])
#print(df.index[count:count*2])
#print(df.index[count*2:count*3])
#print(df.index[count*3:count*4])
#print(df.index[count*4:0])

# 创建新线程
thread1 = Thread_Bll_HisData(df.index[0:count])
thread2 = Thread_Bll_HisData(df.index[count:count*2])
thread3 = Thread_Bll_HisData(df.index[count*2:count*3])
thread4 = Thread_Bll_HisData(df.index[count*3:count*4])
thread5 = Thread_Bll_HisData(df.index[count*4:])
#thread6 = Thread_Bll_HisData(df.index[count*5:count*6])
#thread7 = Thread_Bll_HisData(df.index[count*6:count*7])
#thread8 = Thread_Bll_HisData(df.index[count*7:count*8])
#thread9 = Thread_Bll_HisData(df.index[count*8:count*9])
#thread10 = Thread_Bll_HisData(df.index[count*9:])

#thread8 = Thread_Today_Ticks(stock)
# 开启新线程
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
#thread6.start()
#thread7.start()
#thread8.start()
#thread9.start()
#thread10.start()
#thread8.start()
# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)
threads.append(thread4)
threads.append(thread5)
#threads.append(thread6)
#threads.append(thread7)
#threads.append(thread8)
#threads.append(thread9)
#threads.append(thread10)
#threads.append(thread8)
# 等待所有线程完成
for t in threads:
    t.join()
threads = []
#Insert_Historical_Data(stock,str(time.strftime("%Y-%m-%d", time.localtime())))
#print(ts.get_tick_data(stock,date='2018-12-17')

