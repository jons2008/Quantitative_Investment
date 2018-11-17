import sys
import tushare as ts
import pandas as pd

reload(sys)
sys.setdefaultencoding('utf8')

def Test1(para1,para2):
    df=ts.inst_detail()
    return df

def Test2():
    return '等等我'
