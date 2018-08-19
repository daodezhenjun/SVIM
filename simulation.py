# coding=utf-8
import csv
import datetime as dt
import BSM
from myglobal import *
import math
from IvSample import OptionList
import try1

# 读取 仿真数据并循环写入
today = dt.date(2017, 3, 7)
mature_day = dt.date(2017, 4, 11)
optList = OptionList('m1705', (mature_day - today).days / 365.0, 0.03, 0.6)#days 35
optList.update_future_price(2953)

last_civ=None
last_piv=None

with open('m1705-option.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    count = 0
    a=None

    for row in f_csv:
        opt_quote = Option_quote(row[1].rstrip(), float(row[4]), int(row[11]), float(row[22]), int(row[23]), \
                                 float(row[24]), int(row[25]), row[20], row[21])
        optList.add(opt_quote)

        civ = optList.get_civ()
        if civ != last_civ :
            #TODO get iv smile
            last_civ=civ
        piv = optList.get_piv()
        if piv != last_piv:
            # TODO get iv smile
            last_piv = piv

    try1.testIvSmile(civ+piv)
print "happy end!"
