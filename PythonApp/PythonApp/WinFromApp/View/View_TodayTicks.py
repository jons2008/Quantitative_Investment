import tushare as ts
from Update_Data.BLL.Bll_TodayTicks import Thread_Bll_TodayTicks
class View_TodayTicks():
    def __init__(self,parent=None):
        pass
    def Run(self):
        df = ts.get_stock_basics()
        threads = []
        i=0
        count=int(len(df)/5)
        # 创建新线程
        thread1 = Thread_Bll_TodayTicks(df.index[0:count])
        thread2 = Thread_Bll_TodayTicks(df.index[count:count*2])
        thread3 = Thread_Bll_TodayTicks(df.index[count*2:count*3])
        thread4 = Thread_Bll_TodayTicks(df.index[count*3:count*4])
        thread5 = Thread_Bll_TodayTicks(df.index[count*4:])

        # 开启新线程
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread5.start()

        # 添加线程到线程列表
        threads.append(thread1)
        threads.append(thread2)
        threads.append(thread3)
        threads.append(thread4)
        threads.append(thread5)

        # 等待所有线程完成
        for t in threads:
            t.join()
        threads = []