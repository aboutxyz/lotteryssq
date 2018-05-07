#coding:utf-8

import MySQLdb
import numpy as np
import pandas as pd 
from pandas import Series

db = MySQLdb.connect(host='127.0.0.1',user='root',passwd='900502',db='ssq',port=3306,charset='utf8')
cursor=db.cursor()
data = pd.read_sql(r"select * from ssq",con = db)
ss1 = Series(data.red1)
ss2 = Series(data.red2)
ss3 = Series(data.red3)
ss4 = Series(data.red5)
ss5 = Series(data.red5)
ss6 = Series(data.red6)
print pd.concat([ss1,ss2]).value_counts().values
print sum(pd.concat([ss1,ss2]).value_counts().values)

db.close()