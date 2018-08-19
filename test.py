#!/usr/bin/python

'''
import datetime as dt

spot = 2.483
today = dt.date(2015,1,27)

import csv

with open('option_20150127.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        print (dt.datetime.strptime(row[9], "%Y/%m/%d").date()-today).days/365.0
import math
print math.log(2.71828182846)


a=range(1,10)
def go(x,y):
    print y
    print x+1,"go\n"
    return x+1

map(go,a,a)

b=[6]
print b*10
print  "new"


import ImportTestData
from GaProcess import GaProcess
import numpy as np
import matplotlib.pyplot as plt
from myglobal import *
import SVIM
svi_sample_list=ImportTestData.import_iv()
svim=SVIM.SVIM(svi_sample_list)
print svim.get_iv_smile(svi_param(0, 0.50665225448710813, 0, 0.1, 0.2833052604001267),[-2,-1,-0.5,-0.1,0,0.1,0.5,1,2])

'''


from myglobal import Svi_sample
a=Svi_sample(1,2)
b=Svi_sample(1,2)
print a==b