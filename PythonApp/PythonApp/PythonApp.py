
import tushare as ts
import pandas as pd

df=ts.inst_detail()
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)


print(df)