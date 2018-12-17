from Update_Data.DLL.HistoricalData.HistoricalData import HistoricalData
import threading
import tushare as ts
class Bll_HisData():
    def __init__(self,parent=None):
        pass
    def Insert_Historical_Data(self,code,start,end,ktype):
        CreateTable=HistoricalData()
        if len(CreateTable.Select(ktype=ktype,code=code,start=start,end=end))==0:
            CreateTable.Create(ktype=ktype,code=code)
            CreateTable.Delete(ktype=ktype,code=code,start=start,end=end)
            CreateTable.INSERT(code,start,end,ktype)
            print("开始")
        else:
            print("已经有了"+str(code)+"属性:"+str(ktype))
    

class Thread_Bll_HisData (threading.Thread):
    def __init__(self,code,start,end,ktype):
        threading.Thread.__init__(self)
        self.code1 = code
        self.start1 = start
        self.end1 = end
        self.ktype1=ktype
    def run(self):
       #print "Starting " + self.name
       # 获得锁，成功获得锁定后返回True
       # 可选的timeout参数不填时将一直阻塞直到获得锁定
       # 否则超时后将返回False
        #threadLock.acquire()
        bll_hisdata=Bll_HisData()
        bll_hisdata.Insert_Historical_Data(self.code1,self.start1,self.end1,self.ktype1)
        # 释放锁
        #threadLock.release() 
threadLock = threading.Lock()
    
class Run_Bll_HisData():
    
    def __init__(self,parent=None):
        pass
    def Run_Insert_Historical_Data(self):
        df = ts.get_stock_basics()
        for stock in df.index:
            threads = []
            # 创建新线程
            thread1 = Thread_Bll_HisData(stock,'2005-12-09','2018-12-13','D')
            thread2 = Thread_Bll_HisData(stock,'2005-12-09','2018-12-13','M')
            thread3 = Thread_Bll_HisData(stock,'2005-12-09','2018-12-13','W')
            thread4 = Thread_Bll_HisData(stock,'2005-12-09','2018-12-13','60')
            thread5 = Thread_Bll_HisData(stock,'2005-12-09','2018-12-13','30')
            thread6 = Thread_Bll_HisData(stock,'2005-12-09','2018-12-13','15')
            thread7 = Thread_Bll_HisData(stock,'2005-12-09','2018-12-13','5')
            #thread8 = Thread_Today_Ticks(stock)
            # 开启新线程
            thread1.start()
            thread2.start()
            thread3.start()
            thread4.start()
            thread5.start()
            thread6.start()
            thread7.start()
            #thread8.start()
            # 添加线程到线程列表
            threads.append(thread1)
            threads.append(thread2)
            threads.append(thread3)
            threads.append(thread4)
            threads.append(thread5)
            threads.append(thread6)
            threads.append(thread7)
            #threads.append(thread8)
            
            # 等待所有线程完成
            for t in threads:
                t.join()
            threads = []