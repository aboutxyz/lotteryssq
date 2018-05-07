#coding=utf-8
from __future__ import unicode_literals

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

from pyecharts import Bar

attr = pd.concat([ss1,ss2,ss3,ss4,ss5,ss6]).value_counts(sort = False).index.tolist()
v1 = pd.concat([ss1,ss2,ss3,ss4,ss5,ss6]).value_counts(sort = False).values.tolist()
bar = Bar(u"双色球")
bar.add(u"红球", attr, v1)
bar.render()


db.close()