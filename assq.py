#coding:utf-8

import MySQLdb
import numpy as np
import pandas as pd 

db = MySQLdb.connect(host='127.0.0.1',user='root',passwd='900502',db='ssq',port=3306,charset='utf8')
cursor=db.cursor()
data = pd.read_sql(r"select * from ssq where blue=16",con = db)
print list(data.red1)




db.close()