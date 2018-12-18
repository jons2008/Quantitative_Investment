from Update_Data.DLL.HistoricalData.TodayTicks import TodayTicks
import threading
import tushare as ts
import time
class Bll_TodayTicks():
    def __init__(self,parent=None):
        pass
    def Insert_Historical_Data(self,code):
        CreateTable=TodayTicks()
        if len(CreateTable.Select(code,time.strftime("%Y-%m-%d", time.localtime())))==0:
            #print("开始插入数据："+str(code))
            CreateTable.Create(code)
            CreateTable.Delete(code,date=time.strftime("%Y-%m-%d", time.localtime()))
            CreateTable.INSERT(code)
        else:
            pass
            #print("已经有数据："+str(code))

class Thread_Bll_TodayTicks(threading.Thread):
    def __init__(self,df,ThreadName):
        threading.Thread.__init__(self)
        self.df = df
        self.threadname=ThreadName
    def run(self):
       #print "Starting " + self.name
       # 获得锁，成功获得锁定后返回True
       # 可选的timeout参数不填时将一直阻塞直到获得锁定
       # 否则超时后将返回False
        #threadLock.acquire()
       Numbar=0
       for code in self.df:
           bll_todayticks=Bll_TodayTicks()
           bll_todayticks.Insert_Historical_Data(code)
           Numbar=Numbar+1
           #print("线程名字："+self.threadname+" 开始插入数据："+str(code)+" 数量："+str(Numbar))
           #print(code)
        #bll_hisdata=Bll_HisData()
        #bll_hisdata.Insert_Historical_Data(self.code1,self.start1,self.end1,self.ktype1)
        # 释放锁
        #threadLock.release() 